# -*- coding:utf8 -*-

import requests
import re
import os

url = "http://www.jdxs.cc/book/29075/"
response = requests.get(url)
response.encoding = "gbk"

html = response.text
dl = re.findall(r'<dt class="col-md-12">正文</dt>.*?</dl>', html, re.S)[0]
chapter_info_list = re.findall(r'href="(.*?)" title="(.*?)">', dl, re.S)
# print(chapter_info_list)
title = "苗疆蛊事"
for chapter in chapter_info_list:
        chapter_url, chapter_name = chapter
        chapter_url = "http://www.jdxs.cc/book/29075/%s" % chapter_url
        chapter_response = requests.get(chapter_url)
        chapter_response.encoding = 'gbk'
        chapter_html = chapter_response.text
        chapter_content = re.findall(
            r'经典小说网 www.jdxs.cc，最快更新苗疆蛊事（全16册）最新章节！(.*?)本章未完，点击下一页继续阅读', chapter_html, re.S)[0]
        chapter_content = chapter_content.replace(" ", '')
        chapter_content = chapter_content.replace("&nbsp;", '')
        chapter_content = chapter_content.replace("<br/>", '')
        chapter_content = chapter_content.replace("-->>", '')
        chapter_content = chapter_content.replace("<br><br>", '\n')
        chapter_content = chapter_content.replace("<br", '')

        chapter_path = "d:\\MiaoJiangGuShi\\%s" % chapter_name
        chapter_path = "%s.txt" % chapter_path
        # print(chapter_path)
        f = open(chapter_path,'a',encoding='gbk')
        f.write(chapter_content)
        # with open(chapter_path,'w',encoding='gbk') as f :
        # f.write(chapter_content)
        next_html = re.findall(
            r'<a id="linkNext" class="btn btn-default" href="(.*?)">下一页\(→\)', chapter_html, re.S)[0]
        if len(next_html) != 0:
            chapter_url = next_html
            chapter_name = re.findall(r'<h1 class="readTitle">(.*?) <small>(2/2)</small></h1>',next_html)
            chapter_response = requests.get(chapter_url)
            chapter_response.encoding = 'gbk'
            chapter_html = chapter_response.text
            chapter_content = re.findall(
                r'经典小说网 www.jdxs.cc，最快更新苗疆蛊事（全16册）最新章节！(.*?)</div>', chapter_html, re.S)[0]
            chapter_content = chapter_content.replace(" ", '')
            chapter_content = chapter_content.replace("&nbsp;", '')
            chapter_content = chapter_content.replace("<br/>", '')
            chapter_content = chapter_content.replace("-->>", '')
            chapter_content = chapter_content.replace("<br><br>", '\n')
            chapter_content = chapter_content.replace("<br", '')
            chapter_content = chapter_content.replace("<pclass=\"text-dangertext-centermg0\">", '')
            chapter_path = "d:\\MiaoJiangGuShi\\%s" % chapter_name
            chapter_path = "%s.txt" % chapter_path
            f.write(chapter_content)
        f.close()
        #print(next_html)
        #print("分界线----------------------------------------------------------------------------------------------------------------------")
        # print(chapter_html)
