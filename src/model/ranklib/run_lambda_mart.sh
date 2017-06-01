#!/bin/bash

if [ $# == 0 ]; then
    echo "usage: $0 dataset"
    exit
else
    java -jar RankLib.jar \
        -train ../../../features/$1/train.libsvm \
        -test ../../../features/$1/test.libsvm \
        -save ../../../features/$1/model.lambdamart
        -ranker 6 -metric2t MAP -tvs 0.8 -shrinkage 0.1 
fi

   
