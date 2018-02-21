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
keywords = ['landscape', 'city', 'urban', 'nature', 'mountains', 'sea', 'ocean',
            'night', 'summer', 'winter', 'travel', 'beach', 'abstract', 'universe', 'snow']

help_string = '''randpaper 0.1

Usage: randpaper.py -p <path-to-wallpapers> [-k <search-keyword>]

OPTIONS
 -p          Path to wallpaper dir
 -k          Keyword (optional). If not specified, random keyword from a
             predefined list will be used'''

def parse_args(argv):

    keyword = keywords[random.randrange(0, len(keywords))]
    path = ''

    try:
        opts, args = getopt.getopt(argv, "hp:k:")
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

    if not path:
        print(help_string)
        sys.exit(1)

    return path, keyword

def download_photo(url, path):
    filename = url[url.rfind('/') + 1:]
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(path + filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        return filename
    return False

def find_pic(path, keyword):

    # Basic url
    url = 'https://api.pexels.com/v1/search?query=' + keyword + '&per_page=40&page='

    # Preloading first page
    page_first = url + '1'
    headers = {'Authorization': API_KEY}

    try:
        pre = requests.get(page_first, headers=headers)
        pre_response = json.loads(pre.content)
        # Calculating overall page number
        pages = int(pre_response['total_results'] / 40) + 2

        # Iterating over 5 random pages until a photo with specified dimensions is found
        for i in range(1):
            page_random = url + str(random.randrange(1, pages))

            # Loading and parsing a page
            result = requests.get(page_random, headers=headers)
            response = json.loads(result.content)

            # Iterating over all photos on page
            for p in response['photos']:

                # If a photo doesn't match specified dimensions, continue iterating
                if p['width'] < min_width or p['height'] < min_height:
                    continue

                # Photo is found, download it and return filename
                photo_url = p['src']['original']
                photo_name = photo_url[photo_url.rfind('/') + 1:]

                if photos_local not in photos_local:
                    filename = download_photo(photo_url, path)
                    if filename:
                        return os.path.join(path, filename)

        return False
    except:
        return False

path, keyword = parse_args(sys.argv[1:])
path = os.path.join(path, '')
photos_local = glob.glob1(path, '*.*')

photo_filename = find_pic(path, keyword)
print(photo_filename)

if photo_filename:
    print(photo_filename)
else:
    random_index = random.randrange(1, len(photos_local))
    print(os.path.join(path, photos_local[random_index]))
