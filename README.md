# Kismon

Kismon is GUI client for kismet (wireless scanner/sniffer/monitor) with several features:
* a live map of the networks
* file import: netxml (kismet), csv (old kismet version), json (kismon)
* file export: kmz (Google Earth) and all import formats
* signal graph for each network
* it can connect to multiple kismet servers simultaneously

![Kismon Window](https:/files.salecker.org/kismon/images/0.8/kismon_window.png)

## Dependencies

* kismet
  * Kismon requires the Python module of [kismet](https://github.com/kismetwireless/kismet), it has to be installed for Python 3
* [osm-gps-map](https://github.com/nzjrs/osm-gps-map) (>=1.0.2)
  * osm-gps-map is optional, the map will be disabled if it's missing
* python3-gi, python3-cairo, python3-simplejson
* GTK+ 3

## Kismet Compatibility

Be aware that kismon is starting with version 1.0 not compatible with kismet servers running versions older than 2019-01-beta2.

Here is a list of the known compatibility:

* kismon 1.0.3
  * Kismet 2019-12-R2 - 2020-12-R3
* kismon 1.0.2
  * Kismet 2019-12-R2 - 2020-03-R1
* kismon 1.0.1
  * Kismet 2019-08-R1 - 2019-09-R1
* kismon 1.0.0
  * Kismet 2019-01-beta2 - 2019-04-R1
* kismon 0.9
  * Kismet 2011-01-R1 - 2016-07-R1
* kismon 0.8
  * Kismet 2011-01-R1 - 2014-02-R1

## Installation

```
$ sudo apt-get install git python3 python3-gi gir1.2-gtk-3.0 \
 gir1.2-gdkpixbuf-2.0 python3-cairo python3-simplejson \
 gir1.2-osmgpsmap-1.0
$ git clone https://github.com/Kismon/kismon.git kismon
$ cd kismon
$ python3 setup.py build
$ sudo python3 setup.py install
```

Or just use `make` instead of the python commands.
```
# make install
```

### Kismet Python module

The Python module of kismet isn't included in the most Linux distributions and has to be installed manually.

```
$ git clone https://github.com/kismetwireless/python-kismet-rest.git
$ cd python-kismet-rest
$ sudo python3 setup.py install
```

## Create Debian/Ubuntu package

```
$ sudo apt-get install make debhelper dh-python python3
$ make builddeb
```

## Usage
Launch kismon from the command line after you started kismet or click the the kismon icon in the menu of your desktop environment.

Hotkeys
* Fullscreen:  F11
* Zoom in/out: Ctrl + "i"/"o"

Note: The GPS reciever needs to be setup before running kismon and kismet.

## Links

* Website:         https://www.salecker.org/software/kismon.html
* Git repository:  https://github.com/Kismon/kismon
* References:
* https://www.freecodecamp.org/news/wireless-security-using-raspberry-pi-4-kismet-and-python/
* https://github.com/c-bless/kismetanalyzer
* https://github.com/nattimmis/kismet-modified-range/blob/master/README
* https://en.wikipedia.org/wiki/List_of_WLAN_channels
* https://kismet-rest.readthedocs.io/_/downloads/en/latest/pdf/
* https://github.com/hobobandy/plugin-kismet-creepdetector

## Author
Patrick Salecker <mail@salecker.org>

## License
This project is licensed under BSD, for more details check [COPYING](COPYING).
