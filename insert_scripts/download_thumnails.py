import urllib
import os
import json

path = "data/"

for filename in os.listdir(path):
    video_id = filename.split('.')[0]
    thumbail_url = 'http://i.ytimg.com/vi/' + video_id + '/sddefault.jpg'
    urllib.urlretrieve(thumbail_url, 'images/' + video_id + '.jpg')	