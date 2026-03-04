#!/bin/sh

set -e

# copy submission files that Flask has hopefully written to submission/ dir
cp /submission/dictionary.c /speller/dictionary.c
cp /submission/dictionary.h /speller/dictionary.h

cd /speller
make -B
./speller texts/holmes.txt