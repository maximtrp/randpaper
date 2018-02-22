#!/usr/bin/python3

'''randpaper is a script to download photos with a specified keyword from Pexels
website (https://www.pexels.com/). To use it you must obtain an API KEY from
Pexels (https://www.pexels.com/api/). Put it into a file named as "api.key" near
randpaper.py script or insert below using an API_KEY variable.'''

import requests
import json
import random
import glob
import os
import shutil
import sys
import getopt

# PARAMS
with open(os.path.join(sys.path[0], 'api.key')) as f:
    API_KEY = f.read().strip()
# or comment the above lines and uncomment the following one and specify your key
# API_KEY = ''

min_width = 1920
min_height = 1024

keywords = ['landscape', 'city', 'nature', 'mountains', 'sea', 'ocean', 'pattern',
            'night', 'summer', 'winter', 'travel', 'beach', 'abstract', 'universe',
            'snow', 'road', 'river', 'sky', 'blur', 'stars', 'streets', 'sunset',
            'texture', 'forest', 'rain', 'light']

help_string = '''randpaper 0.2

Usage: randpaper.py -p <path-to-wallpapers> [-a] [-k <search-keyword>] [-n <photos number>]

OPTIONS
 -a          Search within popular photos only (optional)
 -k          Keyword (optional). If not specified, random keyword from a
             predefined list will be used
 -n          Number of photos to download (optional)
 -p          Path to wallpaper dir'''

def parse_args(argv):

    keyword = keywords[random.randrange(0, len(keywords))]
    path = ''
    popular = False
    photos_num = 1

    try:
        opts, args = getopt.getopt(argv, "ahp:k:n:")
    except:
        print(help_string)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(help_string)
            sys.exit()
        elif opt == '-p':
            path = arg
        elif opt == '-k':
            keyword = arg
        elif opt == '-a':
            popular = True
        elif opt == '-n':
            photos_num = int(arg)

    if not path:
        print(help_string)
        sys.exit(1)

    return path, keyword, popular, photos_num

def download_photo(url, path):
    filename = url[url.rfind('/') + 1:]
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(path + filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        return filename
    return False

def find_pic(path, keyword, popular, photos_num):

    # Basic url
    if popular:
        url = 'https://api.pexels.com/v1/popular?per_page=40&page='
    else:
        url = 'https://api.pexels.com/v1/search?query=' + keyword + '&per_page=40&page='

    # Preloading first page
    page_first = url + '1'
    headers = {'Authorization': API_KEY}
    photos = []

    try:
        pre = requests.get(page_first, headers=headers)
        response = json.loads(pre.content)
        # Calculating overall page number
        if not popular:
            pages = int(response['total_results'] / 40) + 2

        # Iterating over 5 random pages until a photo with specified dimensions is found
        for i in range(5):
            if popular:
                page_next = response['next_page']
            else:
                page_next = url + str(random.randrange(1, pages))

            # Loading and parsing a page
            result = requests.get(page_next, headers=headers)
            response = json.loads(result.content)
            page_photos_num = len(response['photos'])

            # Iterating over all photos on page
            for i in range(page_photos_num):

                p = response['photos'][random.randrange(0, page_photos_num)]

                # If a photo doesn't match specified dimensions, continue iterating
                if p['width'] < min_width or p['height'] < min_height:
                    continue

                # Photo is found, download it and return filename
                photo_url = p['src']['original']
                photo_name = photo_url[photo_url.rfind('/') + 1:]

                if photos_local not in photos_local:
                    filename = download_photo(photo_url, path)
                    if filename:
                        photos.append(os.path.join(path, filename))

                    if len(photos) == photos_num:
                        return photos

        return False
    except:
        return False

path, keyword, popular, photos_num = parse_args(sys.argv[1:])
path = os.path.join(path, '')
photos_local = glob.glob1(path, '*.*')
photos = find_pic(path, keyword, popular, photos_num)

if photos:
    print(' '.join(photos))
elif photos_local:
    photos = []
    while len(photos) < photos_num:
        random_index = random.randrange(1, len(photos_local))
        photos.append(os.path.join(path, photos_local[random_index]))
    print(' '.join(photos))
