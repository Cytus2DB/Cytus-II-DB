#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from pydub import AudioSegment

import os, re, sys, json

VERSION = ""

MAX_TIME = 900000000

BASEDATA = "./res/export/assets/game/common/bundleassets/datasheets"
BASEIM   = "./res/export/assets/game/11_im/bundleassets"
BASEOS   = "./res/export/assets/game/15_os/bundleassets"

cnames = {}

"""
File Utils
"""
def getJson(src):
    try:
        with open(src, "rb") as f:
            return json.loads(f.read().decode("utf8"))
    except:
        return []

def putJson(src, content):
    try:
        with open(src, "wb") as f:
            f.write(json.dumps(content, ensure_ascii=False).encode("utf8"))
    except Exception as e:
        print(e)

def loadCache(t, k):
    return getJson("./res/cache_%s_%s.json" % (t, k))

def saveCache(t, k, cache):
    putJson("./res/cache_%s_%s.json" % (t, k), cache)

'''
Image Section
'''
def do_attachments(kind):
    info = kind.split('_')
    cache = loadCache('image', info[1])

    ifolder = './res/export/assets/game/%s/bundleassets/attachments' % kind
    ofolder = './res/converted/images/%sfiles' % info[1]
    
    for i in os.listdir(ifolder):
        # check cache
        if i in cache:
            continue
        im = Image.open('%s/%s/attachment.png' % (ifolder, i))
        # adjust image
        if (im.width == 512 and im.height == 512) or (im.width == 1024 and im.height == 1024):
            im = im.resize((im.width, im.height*3//4))
        elif im.width == 345 and im.height == 512:
            im = im.resize((im.width, im.width))
        elif im.width == 512 and im.height == 435:
            im = im.resize((im.width, im.height*3//4))
        elif im.width == 515 and im.height == 1024:
            im = im.resize((im.width, im.height*7//10))
        else:
            print('%s at %d x %d' % (i, im.width, im.height))
        im.convert('RGB').save('%s/%s.jpg' % (ofolder, i))
        # add cache
        cache.append(i)
    
    saveCache('image', info[1], cache)
    print("Finished Attachments.")

def do_avatars():
    cache = loadCache('image', 'avatars')
    folders = [
        (BASEIM+'/avatars',   './res/converted/images/imavatars'),
        (BASEOS+'/osavatars', './res/converted/images/osavatars')
    ]
    for folder in folders:
        for i in os.listdir(folder[0]):
            ifn = '%s/%s' % (folder[0], i)
            ofn = '%s/%s' % (folder[1], i)
            # check cache
            if ofn in cache:
                continue
            # convert
            Image.open(ifn).save(ofn)
            # add cache
            cache.append(ofn)
    saveCache('image', 'avatars', cache)
    print("Finished Avatars.")

def do_gallery():
    cache = loadCache('image', 'gallery')
    folder = './res/export/assets/game/17_gallery/bundleassets/imageviewer'
    for chara in getJson(BASEDATA+"/gallerydata/folder.txt"):
        for gfile in getJson(BASEDATA+"/gallerydata/%s.txt" % chara["Id"]):
            if gfile["FileLocation"] in cache:
                continue
            if gfile["Format"] == 3:
                sz = gfile["Location"].split(",")
                im = Image.open(folder+'/'+gfile["FileLocation"]+'.png')
                im = im.resize((int(sz[0]), int(sz[1])))
                im.convert('RGB').save('./res/converted/images/gallery/%s.jpg'%gfile["FileLocation"])
                cache.append(gfile["FileLocation"])
    saveCache('image', 'gallery', cache)

def do_imageviewer():
    cache = loadCache('image', 'osspecial')
    folder = BASEOS+'/osimageviewer'
    for i in os.listdir(folder):
        fid = i.split('_')[0]
        ifn = '%s/%s' % (folder, i)
        ofn = './res/converted/images/osspecial/%s.jpg' % i.split('.')[0]
        # check cache
        if ofn in cache:
            continue
        # convert
        im = Image.open(ifn)
        if fid == 'pos2401':
            im = im.resize((im.width, im.height*1080//1920))
        elif fid == 'ros1401':
            im = im.resize((im.width, im.height*4800//7200))
        else:
            print('%s at %d x %d' % (i, im.width, im.height))
        im.convert('RGB').save(ofn)
        # add cache
        cache.append(ofn)
    saveCache('image', 'osspecial', cache)
    print("Finished Imageviewer.")

'''
Audio Section
'''
def do_music():
    cache = loadCache('audio', 'mp3')
    folders = [
        (BASEOS+'/osbgms',   './res/converted/audios/bgms'),
        (BASEOS+'/ossounds', './res/converted/audios/sounds'),
        ('./res/export/audios/story', './res/converted/audios/story'),
        ('./res/export/audios/extra', './res/converted/audios/extra')
    ]
    for folder in folders:
        print("Convert Music [%s]" % folder[0])
        flist = os.listdir(folder[0])
        for i in flist:
            ifn = '%s/%s' % (folder[0], i)
            ofn = '%s/%s.mp3' % (folder[1], i.split('.')[0])
            # progress
            print("Convert Music Progress: [%d/%d]" % (flist.index(i)+1,len(flist)))
            # check cache
            if ofn in cache:
                continue
            # convert
            AudioSegment.from_wav(ifn).export(ofn, bitrate='128k')
            # add cache
            cache.append(ofn)
    saveCache('audio', 'mp3', cache)
    print("Finished Audios.")

'''
Subtitles Section
'''
def srt2vtt(ifn, ofn):
    content = open(ifn, "r", encoding="utf-8").read()
    content = "WEBVTT\n\n" + content
    content = re.sub(r"(\d{2}:\d{2}:\d{2}),(\d{3})",
                     lambda m: m.group(1) + '.' + m.group(2), content)
    open(ofn, "w", encoding="utf-8").write(content)

def do_srt():
    cache = loadCache('data', 'srt')
    srtlangs  = [("en","en"),("ja","ja"),("zh","zh"),("ko","ko"),("zh","zh-TW"),("cn","zh-CN")]
    for lang in srtlangs:
        for i in os.listdir('./res/export/videos'):
            if '.mp4' in i:
                with open(
                 './res/converted/data/subtitles/%s_%s.vtt' % (i.split('.')[0], lang[1]), 'w'
                ) as f:
                    f.write('')
    for lang in srtlangs:
        folder = './res/export/assets/game/common/bundleassets/srtfiles/%s' % lang[0]
        for i in os.listdir(folder):
            ifn = '%s/%s' % (folder, i)
            ofn = './res/converted/data/subtitles/%s_%s.vtt' % (i.split('.')[0], lang[1])
            # check cache
            if ofn in cache:
                continue
            srt2vtt(ifn, ofn)
            # add cache
            cache.append(ofn)
    saveCache('data', 'srt', cache)
    print("Finished Srt.")

"""
Content Utils
"""
def trimContent(content):
    content = re.sub(
        r"<size=(\d+)>",
        lambda x: '<font size="%.1f">' % (int(x.group(1)) * 0.1),
        content,
    )
    content = re.sub(
        r"<color=(#?\w+)>", lambda x: '<font color="%s">' % x.group(1), content
    )
    content = content.replace(
        ">>", "<blockquote>").replace("<<", "</blockquote>")
    content = content.replace(
        "</size>", "</font>").replace("</color>", "</font>")
    return content

def getTime(name):
    time = 0
    name = name.replace("?", "0").replace("X", "0").replace("(","").replace(")","")
    
    r = re.search(r"_(\d{3})_(\d{1,2})_(\d{1,2})(?:_(\d{1,2}))?$", name)
    if r:
        num = r.group(4) if (r.group(4) and r.group(4).isdigit()) else "0"
        time = int(
            "{:0>3d}{:0>2d}{:0>2d}{:0>2d}".format(
                int(r.group(1)), int(r.group(2)), int(r.group(3)), int(num)
            )
        )
    return time if time != 0 else MAX_TIME

def handleiM(iMFile, rk):
    return {
        "id": iMFile["Id"].lower(),
        "rank": rk,
        "avatar": iMFile["AvatarId"].lower(),
        "name": iMFile["CharacterName"],
        "titles": iMFile["Titles"],
        "likes": iMFile["LikeCount"],
        "replies": len(iMFile["Replies"]),
        "version": VERSION
    }

def handleOS(OSContent):
    rows = OSContent.split("##")
    data = list()

    for row in rows:
        package = row.replace("\r", "").split("\n")
        header = package[0].split("=")

        if header[0] == "":
            continue

        attrs = []
        content = None

        if len(header) > 1:
            attrs = header[1].split(",")

        if len(package) > 1:
            content = trimContent("\n".join(package[1:]))

        data.append({"id":len(data) ,"type": header[0], "attrs": attrs, "content": content})

    return data


"""
Modules
"""
def loadChara():
    global cnames
    folder = "./res/export/assets/game/06_result/bundleassets/resultsharesheets"
    for i in os.listdir(folder):
        cdata = getJson("%s/%s" % (folder, i))
        cnames[i.split(".")[0]] = cdata["CharacterName"]

def loadIM():
    cache  = loadCache('data', 'im')
    posts  = getJson("./res/converted/data/imlist.json")
    imlist = getJson(BASEDATA+"/imdata/im_topic_data.txt")
    imlock = getJson(BASEDATA+"/imdata/im_lock_condition_data.txt")
    imrank = {}
    # generate rank
    for ldata in imlock:
        rank = 0
        for lchara in ldata["LevelLocks"]:
            rank += lchara["Level"]
        imrank[ldata["TopicId"].lower()] = rank
    # convert imdata
    for i in imlist:
        # check cache
        if i["Id"].lower() in cache:
            continue
        post = getJson(BASEDATA+"/imdata/imposts/%s/posts.txt" % i["Id"].lower())
        # trim contents
        plist = []
        for pdata in post["Contents"]:
            plist.append(trimContent(pdata))
        # parse replies
        rlist = []
        for reply in post["Replies"]:
            replydata = []
            for rdata in reply["Contents"]:
                replydata.append(trimContent(rdata))
            rlist.append({
                "id": reply["Id"].lower(),
                "name": reply["CharacterName"],
                "avatar": reply["AvatarId"].lower(),
                "contents": replydata,
            })
        putJson(
            "./res/converted/data/imposts/%s.json" % i["Id"].lower(),
            {
                "id": post["Id"].lower(),
                "name": post["CharacterName"],
                "titles": i["Titles"],
                "avatar": post["AvatarId"].lower(),
                "attachments": post["Attachments"],
                "contents": plist,
                "replies": rlist,
            },
        )
        posts.append(handleiM(i, imrank[i["Id"].lower()]))
        cache.append(i["Id"].lower())
    # save data
    posts.sort(key=lambda x: (x["rank"], x["id"]))
    putJson("./res/converted/data/imlist.json", posts)
    saveCache('data', 'im', cache)
    print("Finished iM")

def loadOS():
    res    = getJson(BASEDATA+"/cutscenedata/cutscene_data.txt")
    oslist = getJson("./res/converted/data/oslist.json")
    ostime = []
    if oslist == []:
        oslist = {}
    for cfile in os.listdir(BASEDATA+"/osdata"):
        chara = cfile.split(".")[0].lower()
        cache = loadCache('data', 'os_%s' % chara)
        cdata = getJson(BASEDATA+"/osdata/%s" % cfile)
        if chara in oslist.keys():
            files = oslist[chara]["files"]
        else:
            files = {}

        try:
            os.listdir("./res/converted/data/osfiles/%s" % chara)
        except Exception:
            os.mkdir("./res/converted/data/osfiles/%s" % chara)

        for i in cdata:
            # get time
            time = getTime(i["Names"][0])
            if (time == MAX_TIME) and (len(files) > 0):
                time = ostime[len(ostime) - 1]["time"] + 1
            # put file
            contents = []
            for content in i["Contents"]:
                contents.append(handleOS(content))
            putJson(
                "./res/converted/data/osfiles/%s/%s.json" % (chara, i["Id"].lower()),
                {
                    "id": i["Id"].lower(),
                    "name": i["Names"][0],
                    "res": (
                        res[i["Id"].lower()]["MovieFile"] if i["Id"].lower() in res.keys() else None
                    ),
                    "contents": contents,
                },
            )
            # add to filelist and timelist
            if not i["Id"].lower() in cache:
                files[i["Id"].lower()] = {
                    "name": i["Names"][0],
                    "version": VERSION,
                }
                cache.append(i["Id"].lower())
            ostime.append({
                "id": i["Id"].lower(),
                "time": time,
                "name": i["Names"][0],
                "folder": chara,
                "version": 1,
            })
        oslist[chara] = {"name": cnames[chara], "files": files}
        saveCache('data', 'os_%s' % chara, cache)
    # save data
    ostime.sort(key=lambda x: (x["time"], x["id"].lower()))
    putJson("./res/converted/data/oslist.json", oslist)
    putJson("./res/converted/data/ostime.json", ostime)
    print("Finished OS")

def loadDB():
    dblist = getJson("./res/converted/data/dblist.json")
    if dblist == []:
        dblist = {}
    extrafs = [
        (4, "./res/export/audios/extra", "Extra_Music", "./audios/extra"),
        (5, "./res/export/videos/extra", "Extra_Video", "./videos/extra"),
        (5, "./res/export/videos/titles", "Extra_TitleVideo", "./videos/titles"),
        (5, "./res/export/videos/song_select", "Extra_SongSelect", "./videos/song_select")
    ]
    for chara in getJson(BASEDATA+"/gallerydata/folder.txt"):
        cache = loadCache('data', 'db_%s' % chara["Id"])
        if chara["Id"] in dblist.keys():
            files = dblist[chara["Id"]]["files"]
        else:
            files = {}
        for dbfile in getJson(BASEDATA+"/gallerydata/%s.txt" % chara["Id"]):
            if dbfile["FileName"] in cache:
                continue
            # NEKO special
            if dbfile["FileLocation"] == "nekoHacked(chaosGlitch)":
                dbfile["FileLocation"] = "story_004"
            # add to filelist
            files[dbfile["FileLocation"]] = {
                "name": dbfile["FileName"],
                "type": dbfile["Format"],
                "version": VERSION,
            }
            cache.append(dbfile["FileName"])
        dblist[chara["Id"]] = { "name": chara["Name"], "files": files}
        saveCache('data', 'db_%s' % chara["Id"], cache)
    # Add extra files
    for extraf in extrafs:
        # read cache and init
        cache = loadCache('data', 'db_%s' % extraf[2])
        if extraf[2] in dblist.keys():
            files = dblist[extraf[2]]["files"]
        else:
            files = {}
        for ef in os.listdir(extraf[1]):
            mname = ef.split(".")[0]
            # check cache
            if mname in cache:
                continue
            files[mname] = {
                "name": mname,
                "type": extraf[0],
                "location": extraf[3],
                "version": 1,
            }
        dblist[extraf[2]] = { "name": extraf[2], "files": files}
        saveCache('data', 'db_%s' % extraf[2], cache)
    putJson("./res/converted/data/dblist.json", dblist)
    print("Finished DB")


def main():
    # version sign
    versions = getJson('./res/converted/data/versions.json')
    if VERSION in versions:
        print("Notice: v%s exists" % VERSION)
        return
    versions.append(VERSION)
    putJson('./web/version.json', {"version": VERSION})
    # data
    loadChara()
    loadIM()
    loadDB()
    loadOS()
    # assets
    do_srt()
    do_avatars()
    do_gallery()
    do_imageviewer()
    do_attachments('11_im')
    do_attachments('15_os')
    do_music()
    putJson('./res/converted/data/versions.json', versions)
    # fin
    print("Finished.")


if __name__ == "__main__":
    # define version
    VERSION = sys.argv[1]
    # run
    main()
