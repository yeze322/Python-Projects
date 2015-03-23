#!/bin/bash
mysql --local-infile=1 --user=root --password=950322 --database=Markov<<EOFMYSQL
use Markov
load data local infile '/home/yeze/Desktop/wd/Python-Projects/Markov Analyse/LanguageTextRepertory/MySQL_Import.txt' INTO TABLE word LINES TERMINATED BY '\n';
EOFMYSQL
