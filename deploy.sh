#!/bin/bash

echo "================================="
echo "   Cytus II DB Build Tool V2.0   "
echo "          A.R.C.  Tech.          "
echo "================================="

if [ ! -f "dist.zip" ]; then
  if [ ! $1 ]; then
    echo "Git repo not defined!"
    exit
  fi
  # clone repo
  git clone -n $1 ./dist
  cp -r ./web/dist ./
  cd dist
  # git config
  git config user.name "A.R.C"
  git config user.email "admin@arc.co"
else
  unzip dist.zip
  cd dist
fi

# release
git add . && git commit -m "`date "+[%Y-%m-%d %H:%M] release"`"
git push

# optimize
rm -rf ./*

# clean
cd .. && zip -r dist.zip ./dist && rm -rf ./dist