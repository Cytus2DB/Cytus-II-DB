#!/bin/bash

echo "================================="
echo "   Cytus II DB Build Tool V2.0   "
echo "          A.R.C.  Tech.          "
echo "================================="

# clean
rm -rf ./res/export/*
rm -rf ./res/unitydata/*
rm -rf ./res/unitybundles/*

if [ ! $1 ]; then
  echo "Version not defined!"
  exit
fi

mkdir ./res/export
mkdir ./res/unitydata
mkdir ./res/unitybundles

mkdir ./res/export/audios
mkdir ./res/export/videos
mkdir ./res/export/images
mkdir ./res/export/audios/extra
mkdir ./res/export/audios/story
mkdir ./res/export/videos/extra
mkdir ./res/export/videos/titles
mkdir ./res/export/videos/song_select
mkdir ./res/export/images/characters

echo "Cleaned cache."

# unzip files
unzip -q "./raw/$1.apk" -d ./res/apk
echo "Unziped APK."

# version check
if [ ! -d "./res/apk/assets/bin/" ]; then
  echo "This APK is encrypted!"
  rm -rf "./res/apk"
  exit
fi

# move unity
mv ./res/apk/assets/bin/Data/* ./res/unitydata
echo "Migrated Unity."

# move bundles
mv ./res/apk/assets/AssetBundles/* ./res/unitybundles

# raw assets
mv ./res/apk/assets/RawAssets/*        ./res/export/videos
mv ./res/apk/assets/Titles/*           ./res/export/videos/titles
mv ./res/apk/assets/*_song_select.mp4  ./res/export/videos/song_select
mv ./res/apk/assets/*.mp4              ./res/export/videos/extra
echo "Migrated Raw Assets."

# clean source
rm -rf ./res/apk
echo "Finished."