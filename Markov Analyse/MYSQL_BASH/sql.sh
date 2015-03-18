#!/bin/bash
mysql --local-infile=1 --user=root --password=950322 --database=Markov<<EOFMYSQL
use Markov
load data local infile '/home/yeze/Desktop/wd/Python-Projects/Markov Analyse/bible/a.txt' INTO TABLE A LINES TERMINATED BY '\n';
load data local infile '/home/yeze/Desktop/wd/Python-Projects/Markov Analyse/bible/b.txt' INTO TABLE B LINES TERMINATED BY '\n';
EOFMYSQL
