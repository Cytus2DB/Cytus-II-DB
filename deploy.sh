#!/bin/bash

echo "================================="
echo "   Cytus II DB Build Tool V2.0   "
echo "          A.R.C.  Tech.          "
echo "================================="

#TODO
cd web
npm run build
cd ..
cp -r ./web/build/* ./deploy
rm -rf ./web/build
cd deploy
git add .
git commit -m "`date "+[%Y-%m-%d %H:%M] release"`"
git push
rm -rf `ls`