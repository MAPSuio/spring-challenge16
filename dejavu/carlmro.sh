#!/bin/sh

PITCHES=`cat data.txt | wc -l`

UNIQUE_PITCHES=`cat data.txt | sort | uniq | wc -l`

echo $PITCHES - $UNIQUE_PITCHES | bc
