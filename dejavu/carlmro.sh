#!/bin/sh
sort data.txt | tee sorted.txt | uniq | comm -13 - sorted.txt | wc -l
