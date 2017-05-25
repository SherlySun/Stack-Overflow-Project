#!/usr/bin/env python3

import sys, os
try:
    import ujson as json
except:
    import json

if __name__ == '__main__':
    if len(sys.argv) < 1 + 1:
        print('--usage %s name_of_the_dataset' % sys.argv[0], file=sys.stderr) 
        sys.exit(0)

    # load 
    dataset = sys.argv[1]
    PATH_DATA = '../../data/%s/' % dataset

    # check the existence of the preprocessed question posts
    assert(os.path.exists(PATH_DATA + 'posts_question.json'))

    # count number of questions
    num_line = 0
    with open(PATH_DATA + 'posts_question.json', 'r') as fin:
        for line in fin:
            num_line += 1

    # make 50% of questions for training data
    num_train = num_line // 2
    
    # re-load data and separate into training and testing data
    num_line = 0
    with open(PATH_DATA + 'posts_question.json', 'r') as fin, \
         open(PATH_DATA + 'posts_question_train.json', 'w') as fout_train, \
         open(PATH_DATA + 'posts_question_test.json', 'w') as fout_test:
        for line in fin:
            print(line, end='', file=fout_train if num_line < num_train else fout_test)
            num_line += 1
            
                

    
