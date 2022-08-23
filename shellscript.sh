#!/bin/sh

cd ~/Documents/Git/mirinae-website-search

cat_beginning='python mirinae-website-search.py --url '
cat_end='; exit'

nix-shell --command "${cat_beginning}\"${1}\"${cat_end}"