#!/usr/bin/env python3

import sys, os
import re
from lxml import etree
#from xml.etree import cElementTree
from html2text import html2text
from html.parser import HTMLParser
try:
    import ujson as json
except:
    import json

def preprocess_posts(PATH_RAW, PATH_DATA):
    html_parser = HTMLParser()
    parser = etree.iterparse(PATH_RAW + 'Posts.xml', events=('end',), tag='row')
    with open(PATH_DATA + 'posts_question.json', 'w') as fout_q, \
         open(PATH_DATA + 'posts_answer.json', 'w') as fout_a:
        for event, elem in parser:
            attr = dict(elem.attrib)
            attr['Body'] = html2text(html_parser.unescape(attr['Body']))
            print(json.dumps(attr), file=fout_q if attr['PostTypeId'] == '1' else fout_a)
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]

if __name__ == '__main__':
    if len(sys.argv) < 1 + 1:
        print('--usage %s [name of dataset]' % sys.argv[0], file=sys.stderr) 
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
