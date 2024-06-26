# Kismon2

Kismon2 is a GUI client for kismet (wireless scanner/sniffer/monitor) forked from the original Kismon, with several features:
* A live map of devices
* File import: netxml (kismet), csv (old kismet version), json (kismon)
* File export: kmz (Google Earth) and all import formats
* Signal graph for each network
* It can connect to multiple kismet servers simultaneously
* Filters for different device types

Future Improvements will include:
* Many GUI and basic function improvements (currently ongoing as of June 2024)
* Analysis Functions:
<br> - Geofencing areas, to include device matching over multiple locations (halfway there, June 2024)
<br> - New device alerts
<br> - Patterns over time of individual devices (seen at odd times, repeated arrive/depart events)
<br> - Aproximate locations in reference to the kismet server device
* De-randmization of MAC addresses utlizing probe request signatures
* Incorporation of bluetooth, and other RF signals (via HackRF, etc)

![Kismon Window](https:/files.salecker.org/kismon/images/0.8/kismon_window.png)

## Dependencies

* kismet
  * Kismon requires the Python module of [kismet](https://github.com/kismetwireless/kismet), it has to be installed for Python 3
* [osm-gps-map](https://github.com/nzjrs/osm-gps-map) (>=1.0.2)
  * osm-gps-map is optional, the map will be disabled if it's missing
* python3-gi, python3-cairo, python3-simplejson
* GTK+ 3

## Installation

```
$ sudo apt-get install git python3 python3-gi gir1.2-gtk-3.0 \
 gir1.2-gdkpixbuf-2.0 python3-cairo python3-simplejson \
 gir1.2-osmgpsmap-1.0
$ git clone https://github.com/devintrowbridge/kismon.git kismon
$ cd kismon
$ python3 setup.py build
$ sudo python3 setup.py install
```

Or just use `make` instead of the python commands.
```
# make install
```

### Kismet Python module

The Python module of kismet isn't included in most Linux distributions and has to be installed manually.

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
Launch kismon2 from the command line after you've started kismet or click the the kismon2 icon in the menu of your desktop environment.

Hotkeys
* Fullscreen:  F11
* Zoom in/out: Ctrl + "i"/"o"

Note: The GPS reciever needs to be setup before running kismon2 and kismet.

## Links

* Original Website:         https://www.salecker.org/software/kismon.html
* Original Git repository:  https://github.com/Kismon/kismon

## Original Author
Patrick Salecker <mail@salecker.org>
<br> This Fork: Devin Trowbridge && CrystalHeeler

## License
This project is licensed under BSD, for more details check [COPYING](COPYING).
