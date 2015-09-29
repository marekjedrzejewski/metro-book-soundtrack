import itertools
import urllib.request
from os.path import normpath, exists
from os import makedirs

# directory to save downloaded tracks
savedir = "metro_playlist"

# track names format elements
fmt_chapter = "{:02d}"
fmt_fragment = "{:d}"
fmt_trackname = fmt_chapter + "-" + fmt_fragment

website_root = "http://m-e-t-r-o.ru/"
track_extension = ".mp3"

# chapters and fragments don't start with 0.
start = 1

if not exists(savedir):
    makedirs(savedir)

for chapter in itertools.count(start):
    downloaded_things = False
    for fragment in itertools.count(start):
        trackname = fmt_trackname.format(chapter, fragment) + track_extension
        trackaddress = website_root + trackname
        target = savedir + "/" + trackname
        try:
            urllib.request.urlretrieve(trackaddress, normpath(target))
        except:
            break
        print(target, "saved")
        downloaded_things = True
    # if nothing was downloaded, that's the end
    if not downloaded_things:
        break
