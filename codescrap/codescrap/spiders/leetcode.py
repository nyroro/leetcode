# -*- coding: utf-8 -*-
import scrapy
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import os
ptn = re.compile(r'^\s*submissionCode.*?,$')
class LeetcodeSpider(scrapy.Spider):
    name = 'leetcode'
    allowed_domains = ['leetcode.com']
    start_urls = 'https://leetcode.com/api/problems/all/'

    def start_requests(self):
        self.cookie = {}
        self.exists = set()
        if os.path.exists('ac_code'):
            files = os.listdir('ac_code')
            for file in files:
                self.exists.add(int(file[2:file.index('.')]))
            
        with open("cookie.txt", 'r') as f:
            for line in f:
                k,v = line.split()
                self.cookie[k] = v
        print 'cookie',self.cookie
        yield scrapy.Request(self.start_urls, cookies=self.cookie)

    def get_submission_url(self, data):
        print data
        name = data['stat']['question__title_slug']
        sub_url = 'https://leetcode.com/graphql'
        method = 'POST'
        headers = {
'Connection'	:'keep-alive',
'content-type':	'application/json',
'Referer':'https://leetcode.com/problems/%s/submissions/'%name	,
        }
        variables = {
            'lastKey': None,
            'limit': 20,
            'offset': 0,
            'questionSlug': name
        }

        body = {
            'operationName':'Submissions',
            'query':'query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {    lastKey    hasNext    submissions {      id      statusDisplay      lang      runtime      timestamp      url      isPending      memory      __typename    }    __typename  }}',
            'variables': variables
        }
        return scrapy.Request(sub_url, method = method, headers=headers, body = json.dumps(body), cookies=self.cookie, callback=self.parse_submission, meta={'id':data['stat']['question_id']})
        # return scrapy.Request('https://leetcode.com/problems/%s/submissions/'%name, cookies = self.cookie)
    def parse(self, response):
        data = json.loads(response.text)
        for t in data['stat_status_pairs']:
            if t['status'] == 'ac' and t['stat']['question_id'] not in self.exists:
                yield self.get_submission_url(t)
                # break

    def parse_submission(self, response):
        data = json.loads(response.text)
        # print data
        # yield data
        id = response.meta['id']
        accepts = [t for t in data["data"]['submissionList']["submissions"] if t['statusDisplay'] == 'Accepted']
        sub_id = accepts[0]['id']
        lang = accepts[0]['lang']
        url = 'https://leetcode.com/submissions/detail/%s/'%sub_id
        meta = {'id':id, 'lang':lang}
        yield scrapy.Request(url, cookies=self.cookie, callback=self.parse_submit_detail, meta = meta)

    def parse_submit_detail(self, response):
        
        index = response.text.find('submissionCode: ') + len('submissionCode: ')
        end = response.text.find(',\n', index)
        code = eval('u'+response.text[index:end])
        meta = response.meta
        meta['code']= code
        yield meta
