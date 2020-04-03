#!/bin/bash

echo "================================="
echo "   Cytus II DB Build Tool V2.0   "
echo "          A.R.C.  Tech.          "
echo "================================="

# clean
rm -rf ./res/export
rm -rf ./res/unitydata
rm -rf ./res/unitybundles

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
mkdir ./res/export/videos/story
mkdir ./res/export/videos/extra
mkdir ./res/export/videos/titles
mkdir ./res/export/videos/song_select
mkdir ./res/export/images/characters

echo "Cleaned cache."

# unzip files
unzip -q "./raw/$1.apk" -d ./res/apk
echo "Unziped APK."

unzip -q "./raw/$1.obb" -d ./res/obb
echo "Unziped OBB."

# move unity
mv ./res/apk/assets/bin/Data/* ./res/unitydata
mv ./res/obb/assets/bin/Data/* ./res/unitydata
echo "Migrated Unity."

# move obb
mv ./res/obb/assets/AssetBundles/* ./res/unitybundles

# obb.raw
rm -rf ./res/obb/assets/RawAssets/Click*.mp4

if [ -d "./res/obb/assets/bin/" ]; then
  rm -rf ./res/obb/assets/RawAssets/GamePlayBGVideo/FinalBossStage.mp4
  mv ./res/obb/assets/RawAssets/GamePlayBGVideo/*.mp4 ./res/export/videos/story
  rm -rf ./res/obb/assets/RawAssets/GamePlayBGVideo
fi

mv ./res/obb/assets/RawAssets/*_ending*.mp4 ./res/export/videos/story
mv ./res/obb/assets/RawAssets/*Cutscene.mp4 ./res/export/videos/story
mv ./res/obb/assets/RawAssets/eos*.mp4      ./res/export/videos/story

mv ./res/obb/assets/RawAssets/*        ./res/export/videos
mv ./res/obb/assets/Titles/*           ./res/export/videos/titles
mv ./res/obb/assets/*_song_select.mp4  ./res/export/videos/song_select
mv ./res/obb/assets/*.mp4              ./res/export/videos/extra
echo "Migrated OBB."

# clean source
rm -rf ./res/apk ./res/obb
echo "Finished."