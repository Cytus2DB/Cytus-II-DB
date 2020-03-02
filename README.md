# Cytus II DB

Knowledge database maintained by A.R.C.

Donate: [爱发电](https://afdian.net/@dtsdao) / [Patreon](https://www.patreon.com/dtsdao).

## Requirements

This program can be executed on Linux/Windows/macOS.

You must have at least 2 GB free space on your current disk.

Make sure you have installed these softwares on your PC:

- Git
- Zip
- Bash
- FFmpeg
- Node.js
- Python 3 with `pydub` and `Pillow`
- [AssetStudio](https://github.com/Perfare/AssetStudio)

## Compile

Compiling is not the "compiling", it means translating the original files to readable datasheets.

It can be accomplished easily with tools here.

### Google Play Version

1. Clone this project with `git`.
2. Put your `.obb` file into `./raw` and rename to `{version}.obb`
3. Put your `.apk` file into `./raw` and rename to `{version}.apk`
4. Execute `./asset.sh {version}`
5. Use AssetStudio to export files as below
6. Execute `./build.sh {version}`
7. Release your generated website.

### Longyuan Version / 龙渊版

**注意：龙渊对某些版本进行了加密，本自动化处理程序将无法支持，请自行解决资源提取问题**

1. 用 `git` 克隆本项目
2. 将游戏资源导出至计算机中（未加密版本可使用 `./china.sh {version}` ）
3. 按照下方说明使用 AssetStudio 导出文件
4. 运行 `./build.sh {version}`
5. 发布你编译的网页

## Clean

If you did anything wrong or you just want a fresh start, execute `./clean.sh`

But as the version data is stored in cache, this shouldn't be operated unless you keep your old version, or your update log will be lost.

BTW, the stored files are `./res/converted/*` and `./res/cache_*.json`, you can delete the cache data of any certain module as you wish.

## Export Instruction

1.  Load folder `./res/unitybundles`
2.  Enable `Options > Display all assets`
3.  Enable `Options > Display asset original name`
4.  Enable `Options > Do not group`
5.  Enable `Options > Export options > Convert Texture2D(PNG)`
6.  Filter `AudioClip`, `TextAsset`, `Sprite`
7.  `Export > Filtered assets` to `./res/export`
8.  Restart(close&open) AssetStudio 
9.  Load folder `./res/unitydata`
10. Export `Sprite` : `{character}_s` to `./res/export/images/characters`
11. Export `AudioClip` : `story_*` to `./res/export/audios/story`
12. (Optional) Export `AudioClip` : `title*`, `{character}_*` (Larger ones are full-versions) to `./res/export/audios/extra`

## Deploy To Github Pages

Make sure you had added your ssh keys to your Github account.

1. Configure your git info in `./deploy.sh`
2. Execute `./deploy.sh {git_repo}`

## Announcement

**None of the repo, the tool, nor the repo owner is affiliated with, or sponsored or authorized by, Rayark Inc. or its affiliates.**