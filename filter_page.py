#! /usr bin/python
# -*- coding: utf-8 -*-
#
# How to RUN: 
# 1) Right-click anywhere in the editor window and select Run Python File in Terminal / "Python Datei im Terminal ausführen" 
# 2) mark lines, shift + enter
#    Select one or more lines, then press Shift+Enter or right-click and select Run Selection/Line in Python Terminal. 
#    This command is convenient for testing just a part of a file.
# 3) From the Command Palette (Ctrl+Shift+P), select the Python: Start REPL command to open a REPL terminal for the currently selected Python interpreter. 
#    In the REPL, you can then enter and run lines of code one at a time.

# Define a function get_urls(url) which searches a given page and  
# returns a list of URLs. With each URL a list of keywords associated with
# this URL is returned.
# (Keywords is the link text splitted into words.)
# Hint: Have a look at:
# https://pypi.python.org/pypi/beautifulsoup4
# https://requests.readthedocs.io/



# https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
import requests
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

class Url: 
    # Todo: 1.  load page
    #       1.1 python -m pip install requests
    def get_urls(self, url): 
        req = requests.post(url)
        page_text = BeautifulSoup(req.text, 'html.parser')
        link_url_list = list()
        link_url_keyword_list = list()  # [(link_url1,[keyword1.1,..]), (link_url2,[keyword2.1,..])]}
        if req.status_code != 200:
            print(req.status_code)

        # Todo: 2.  filter all links out of page
        #       2.1 pip install beautifulsoup4 
        for link in page_text.find_all('a'):
            link_url = link.get('href') 
            # print(link.get('href'))
            link_url_list.append(link_url)

        # Todo: 3. filter all keywords out of all links
        for link_url in link_url_list:
            if link_url: 
            # avoid error 'nontype'
                keyword_list = link_url.split('/')
                link_url_keyword_list.append((link_url, keyword_list))     

        # Todo: 4. build list of Urls associated with its keywords  
        for link_keyword_tupel in link_url_keyword_list:
            print(link_keyword_tupel, '\n')

    
request = Url()
request.get_urls('https://www.tagesschau.de/')



