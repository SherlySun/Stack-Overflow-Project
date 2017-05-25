# UCLA 17S CS 249 Final Project 

## Overall Framework 

1. Feature Extraction
2. Learning-to-Rank

## Implemented Features

* User Features
    * user_age
    * user_badge
* Post Features
    * comment_cnt




## Instructions

### Preprocessing
```bash
cd src/preprocess
./preprocess.py [name of dataset]
```

## Directory Descriptions

Here some descriptions briefly show the purpose of each directory.

* __raw/__: The directory for the raw data (i.e., *Posts.xml*, *Users.xml*, etc) 
    * __raw/[name of dataset]/__: the corresponding raw data for a certain dataset (e.g., *StackOverflow*)
    * Note that the file names should not be modified.
* __data/__: The directory for the preprocessed data
    * __data/[name of dataset]/__: the corresponding preprocessed data for a certain dataset (e.g., *StackOverflow*)
* __src/__: The directory for all source codes
    * __src/preprocess/__: Codes for preprocessing raw data