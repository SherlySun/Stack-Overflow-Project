#!/bin/bash

if [ $# == 0 ]; then
    echo "usage: $0 dataset"
    exit
else
    java -jar RankLib.jar -train ../../../features/mathoverflow/train.libsvm -test ../../../features/mathoverflow/test.libsvm -ranker 6 -metric2t MAP -tvs 0.8 -shrinkage 0.1
fi

   
