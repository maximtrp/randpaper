# randpaper

_randpaper_ is a Python script to download photos tagged with a specified keyword from [Pexels](https://www.pexels.com/) website.

To use it you must obtain an _API KEY_ from [Pexels](https://www.pexels.com/api/). Put it into `api.key` file near `randpaper.py` script or insert it below using an API_KEY variable.

## Requirements

_randpaper_ uses the following Python packages from the standard library: `json`, `random`, `glob`, `os`, `shutil`, `sys`, `getopt`. You must also install [requests](http://python-requests.org/) package.

## Usage example

```
$ ./randpaper.py -p ~/Pictures/Wallpapers/
```

## Using with i3

I personally use this script with i3 to get a random photo and set it as a wallpaper.

Using [feh](https://feh.finalrewind.org/) and _randpaper_ from a command line:

```
$ feh --bg-fill $(./randpaper.py -p ~/Pictures/Wallpapers/ -k tech)
```

Setting a shortcut inside i3 config file:

```
bindsym $mod+Print exec --no-startup-id "feh --bg-fill $(~/Programming/randpaper/randpaper.py -p ~/Pictures/Wallpapers/)"
```
