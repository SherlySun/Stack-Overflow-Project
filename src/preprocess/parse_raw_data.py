#!/usr/bin/env python3

import sys, os
import re
from lxml import etree
#from xml.etree import cElementTree
from html2text import html2text
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import nltk

# lxml.html.document_fromstring(html_string)

try:
    import ujson as json
except:
    import json

def clean_html(x):
    return BeautifulSoup(x, 'lxml').get_text()

def preprocess_general(PATH_RAW, PATH_DATA, raw_file, output_file):
    html_parser = HTMLParser()
    parser = etree.iterparse(PATH_RAW + raw_file, events=('end',), tag='row')
    with open(PATH_DATA + output_file, 'w') as fout:
        for event, elem in parser:
            attr = dict(elem.attrib)
            print(json.dumps(attr), file=fout)
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]

def preprocess_posts(PATH_RAW, PATH_DATA):
    html_parser = HTMLParser()
    parser = etree.iterparse(PATH_RAW + 'Posts.xml', events=('end',), tag='row')
    with open(PATH_DATA + 'posts_question.json', 'w') as fout_q, \
         open(PATH_DATA + 'posts_answer.json', 'w') as fout_a:
        for event, elem in parser:
            attr = dict(elem.attrib)
            attr['Body'] = clean_html(attr['Body'])
            if attr['PostTypeId'] == '1':
                print(json.dumps(attr), file=fout_q)
            elif attr['PostTypeId'] == '2':
                print(json.dumps(attr), file=fout_a)

            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]

def preprocess_comments(PATH_RAW, PATH_DATA):
    html_parser = HTMLParser()
    parser = etree.iterparse(PATH_RAW + 'Comments.xml', events=('end',), tag='row')
    with open(PATH_DATA + 'comments.json', 'w') as fout:
        for event, elem in parser:
            attr = dict(elem.attrib)
            attr['Text'] = html_parser.unescape(attr['Text'])
            print(json.dumps(attr), file=fout)
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]


if __name__ == '__main__':
    if len(sys.argv) < 1 + 1:
        print('--usage %s name_of_the_dataset' % sys.argv[0], file=sys.stderr) 
        sys.exit(0)

    # load 
    dataset = sys.argv[1]
    PATH_RAW = '../../raw/%s/' % dataset
    PATH_DATA = '../../data/%s/' % dataset

    # check the existence of the raw data
    assert(os.path.isdir(PATH_RAW))
    
    # create the corresponding directory for preprocessed data
    if not os.path.isdir(PATH_DATA):
        os.makedirs(PATH_DATA)

    # start preprocessing 
    preprocess_posts(PATH_RAW, PATH_DATA)
    preprocess_comments(PATH_RAW, PATH_DATA)
    preprocess_general(PATH_RAW, PATH_DATA, 'Badges.xml', 'badges.json')
    preprocess_general(PATH_RAW, PATH_DATA, 'PostLinks.xml', 'postlinks.json')
    preprocess_general(PATH_RAW, PATH_DATA, 'Tags.xml', 'tags.json')
    preprocess_general(PATH_RAW, PATH_DATA, 'Users.xml', 'users.json')
    preprocess_general(PATH_RAW, PATH_DATA, 'Votes.xml', 'votes.json')
    preprocess_general(PATH_RAW, PATH_DATA, 'PostHistory.xml', 'posthistory.json')
