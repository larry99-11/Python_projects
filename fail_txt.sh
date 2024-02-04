#!/bin/bash 

#we want to see the contents of log.txt and look for any 'fails'

grep -i "Fail" log.txt > fail.txt 

if [ -s fail.txt ]; then
    cat fail.txt
    echo 'Results saved in fail.txt'
else
    #removing file if nothing inside
    rm fail.txt
    echo 'fail.txt was empty and has been removed!'
fi

# add eog command later on