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
    assert(os.path.exists(PATH_DATA + 'question_answer_mapping.json'))
    
    # load question-answer mapping
    instances = [] 
    with open(PATH_DATA + 'question_answer_mapping.json', 'r') as fin:  
        for line in fin:
            data = json.loads(line)
            instances.append(data)
    
    # 50% former instances are training data
    num_train = len(instances) // 2

    train_id = set()
    for i in range(num_train):
        train_id.add(instances[i]['QuestionId'])

    # dump train/test mappings
    with open(PATH_DATA + 'train.question_answer_mapping.json', 'w') as fout:
        for i in range(num_train):
            if instances[i]['AcceptedAnswerId'] != None and len(instances[i]['AnswerList']) > 1:
                print(json.dumps(instances[i]), file=fout)
    with open(PATH_DATA + 'test.question_answer_mapping.json', 'w') as fout:
        for i in range(num_train, len(instances)):
            if instances[i]['AcceptedAnswerId'] != None and len(instances[i]['AnswerList']) > 1:
                print(json.dumps(instances[i]), file=fout)
    
    # dump train/test question and answer posts
    with open(PATH_DATA + 'posts_question.json', 'r') as fin, \
         open(PATH_DATA + 'train.posts_question.json', 'w') as fout_train, \
         open(PATH_DATA + 'test.posts_question.json', 'w') as fout_test:
        for line in fin:
            data = json.loads(line)
            print(line, end='', file=fout_train if data['Id'] in train_id else fout_test)

    with open(PATH_DATA + 'posts_answer.json', 'r') as fin, \
         open(PATH_DATA + 'train.posts_answer.json', 'w') as fout_train, \
         open(PATH_DATA + 'test.posts_answer.json', 'w') as fout_test:
        for line in fin:
            data = json.loads(line)
            print(line, end='', file=fout_train if data['ParentId'] in train_id else fout_test)


