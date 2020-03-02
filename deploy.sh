#!/bin/bash

echo "================================="
echo "   Cytus II DB Build Tool V2.0   "
echo "          A.R.C.  Tech.          "
echo "================================="

username  = "A.R.C"
useremail = "admin@arc.co"

# clone repo
git clone -n $1 ./dist
cp -r ./web/dist ./
cd dist

# git config
git config user.name $username
git config user.email $useremail

# release
git add . && git commit -m "`date "+[%Y-%m-%d %H:%M] release"`"
git push

# clean
cd .. && rm -rf ./dist