# Cytus II DB

Knowledge database maintained by A.R.C.

Donate: [爱发电](https://afdian.net/@dtsdao) / [Patreon](https://www.patreon.com/dtsdao).

## Requirements

This program can be executed on Linux/Windows/macOS.

You must have at least 5 GB free space on your current disk.

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

If you want to release your generated website at current version, just add `dist` after the 6th step.

### Longyuan Version / 龙渊版

**注意：龙渊对某些版本进行了加密，本自动化处理程序将无法支持，请自行解决资源提取问题**

1. 用 `git` 克隆本项目
2. 将游戏资源导出至计算机中（未加密版本可使用 `./china.sh {version}` ）
3. 按照下方说明使用 AssetStudio 导出文件
4. 运行 `./build.sh {version}`

如果希望生成这个版本的发布版，请在第4步后添加 `dist`。

## Clean

If you did anything wrong or you just want a fresh start, execute `./clean.sh`

But as the version data is stored in cache, this shouldn't be operated unless you keep your old version, or your update log will be lost.

BTW, the stored files are `./res/converted/*` and `./res/cache_*.json`, you can delete the cache data of any certain module as you wish.

## Export Instruction

1.  Enable the following options in `Options` menu.
- `Display all assets`
- `Display asset information(original name)`
- `Convert Texture2D(PNG)`
- `Group > Do not group`
2.  Load folder `./res/unitybundles`
3.  Filter `AudioClip`, `TextAsset`, `Sprite`
4.  `Export > Filtered assets` to `./res/export`
5.  Restart(close&open) AssetStudio 
6.  Load folder `./res/unitydata`
7.  Export `Sprite` : `{character}_s` to `./res/export/images/characters`
8.  Export `AudioClip` : `story_*` to `./res/export/audios/story`
9.  (Optional) Export `AudioClip` : `title*`, `{character}_*` (Larger ones are full-versions) to `./res/export/audios/extra`

## Deploy To Github Pages

Make sure you had added your ssh keys to your Github account.

To deploy, configure your git info in `./deploy.sh` and execute it.

## Announcement

**None of the repo, the tool, nor the repo owner is affiliated with, or sponsored or authorized by, Rayark Inc. or its affiliates.**