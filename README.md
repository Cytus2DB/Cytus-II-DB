# Cytus II DB

Knowledge database maintained by A.R.C.

Donate [here](https://afdian.net/@dtsdao).

## Requirements

- Git
- Zip
- Bash
- FFmpeg
- Node.js
- Python 3 with `pydub` and `Pillow`
- [AssetStudio](https://github.com/Perfare/AssetStudio)

## Compile

### GooglePlay Version

1. Clone this project with `git`.
2. Put your `.obb` file into `./raw` and rename to `cytus.obb`
3. Put your `.apk` file into `./raw` and rename to `cytus.apk`
4. Execute `./asset.sh`
5. Use AssetStudio to export files as below
6. Execute `./build.sh`
7. Release your generated website.

### Longyuan Version/龙渊版:

**注意：龙渊有些版本进行了加密，本自动化处理程序将无法支持，请自行解决资源提取问题**

1. 用 `git` 克隆本项目
2. 将游戏资源导出至计算机中（未加密版本可使用 `./china.sh` ）
3. 按照下方说明使用 AssetStudio 导出文件
4. 运行 `./build.sh`
5. 发布你编译的网页

## Export Instruction

1.  Load folder `./res/unitybundles`
2.  Enable `Options > Display all assets`
3.  Enable `Options > Display asset original name`
4.  Enable `Options > Do not group`
5.  Enable `Options > Export options > Convert Texture2D(PNG)`
6.  Filter `AudioClip`, `TextAsset`, `Sprite`
7.  `Export > Filtered assets` to `./res/export`
8.  Restart AssetStudio
9.  Load folder `./res/unitydata`
10. Export `Sprite` : `{character}_s` to `./res/export/images/characters`
11. Export `AudioClip` : `story_*` to `./res/export/audios/story`
12. (Optional) Export `AudioClip` : `title*`, `{character}_*` (Larger ones are full-versions) to `./res/export/audios/extra`

## Deploy To Github Pages

Clone your repo to `./deploy` and execute `./deploy.sh`

## Announcement

**None of the repo, the tool, nor the repo owner is affiliated with, or sponsored or authorized by, Rayark Inc. or its affiliates.**