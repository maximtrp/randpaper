# randpaper

_randpaper_ is a Python script to download photos tagged with a specified keyword (or a random one from the predefined list) from [Pexels](https://www.pexels.com/) website.

To use it you must obtain an _API KEY_ from [Pexels](https://www.pexels.com/api/). Put it into `api.key` file near `randpaper.py` script or insert it below using an API_KEY variable.

## Requirements

_randpaper_ uses the following Python packages from the standard library: `json`, `random`, `glob`, `os`, `shutil`, `sys`, `getopt`. You must also install [requests](http://python-requests.org/) package.

## Help string

Run with `-h` flag to see help string:

```
$ chmod +x randpaper.py
$ ./randpaper.py -h
Usage: randpaper.py [options]

Options:
  -h, --help  show this help message and exit
  -a          search within popular photos only (optional)
  -k KEYWORD  keyword (default - choose one from a predefined list)
  -n NUMBER   number of photos to download (default = 1)
  -p PATH     path to wallpaper dir
```

## Usage examples

Download a photo tagged with a random keyword (from the predefined list) and put it into `~/Pictures/Wallpapers/` directory:

```
$ ./randpaper.py -p ~/Pictures/Wallpapers/
```

Download two photos:

```
$ ./randpaper.py -p ~/Pictures/Wallpapers/ -n 2
```

Download two _popular_ photos:

```
$ ./randpaper.py -p ~/Pictures/Wallpapers/ -n 2 -a
```

Using [feh](https://feh.finalrewind.org/) and _randpaper_ from a command line:

```
$ feh --bg-fill $(./randpaper.py -p ~/Pictures/Wallpapers/ -k tech)
```

## Using with i3

I personally use this script with [i3](https://i3wm.org/) to get a random photo and set it as a wallpaper.
Setting a keyboard shortcut inside i3 `config` file:

```
bindsym $mod+Print exec --no-startup-id "feh --bg-fill $(~/Programming/randpaper/randpaper.py -p ~/Pictures/Wallpapers/)"
```

## Limits

[Pexels API](https://www.pexels.com/api/) imposes certain limits on requests number per hour and month: 200 and 20000.
