# randpaper

_randpaper_ is a Python script to download photos tagged with a specified keyword (or a random one from the predefined list) from [Pexels](https://www.pexels.com/) website.

To use it you must obtain an _API KEY_ from [Pexels](https://www.pexels.com/api/). Put it into `api.key` file near `randpaper.py` script or insert it below using an API_KEY variable.

## Requirements

_randpaper_ uses the following Python packages from the standard library: `json`, `random`, `glob`, `os`, `shutil`, `sys`, `getopt`. You must also install [requests](http://python-requests.org/) package.

## Usage examples

Download a photo tagged with a random keyword (from the predefined list) and put it into `~/Pictures/Wallpapers/` directory:

```
$ chmod +x randpaper.py
$ ./randpaper.py -p ~/Pictures/Wallpapers/
```

Download two photos:

```
$ chmod +x randpaper.py
$ ./randpaper.py -p ~/Pictures/Wallpapers/ -n 2
```

Download two _popular_ photos:

```
$ chmod +x randpaper.py
$ ./randpaper.py -p ~/Pictures/Wallpapers/ -n 2 -a
```

## Using with i3

I personally use this script with [i3](https://i3wm.org/) to get a random photo and set it as a wallpaper.

Using [feh](https://feh.finalrewind.org/) and _randpaper_ from a command line:

```
$ feh --bg-fill $(./randpaper.py -p ~/Pictures/Wallpapers/ -k tech)
```

Setting a keyboard shortcut inside [i3](https://i3wm.org/) `config` file:

```
bindsym $mod+Print exec --no-startup-id "feh --bg-fill $(~/Programming/randpaper/randpaper.py -p ~/Pictures/Wallpapers/)"
```

## Limits

[Pexels API](https://www.pexels.com/api/) imposes certain limits on requests number per hour and month (200 and 2000).
