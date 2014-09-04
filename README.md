**xyz2wmts** - version beta

xyz2wmts helps you to start providing WMTS by generating service metadata.

# How to use?
 1. generate XYZ tiles using a tile generator such as [MapTiler](http://www.maptiler.org/).
 2. edit `settings.py` and add your layer definitions into it.
 3. run `python xyz2wmts.py > WMTSCapabilities.xml`.
 4. upload tiles and WMTSCapabilities.xml to a web server.

## sample WMTS

Metadata URL is https://dl.dropboxusercontent.com/u/21526091/wmts/WMTSCapabilities.xml

Layer

* SRTM3 SHADED RELIEF (JAPAN)

 Shaded relief map made with SRTM3 data.

# License
MIT License

_Copyright (c) 2014, Minoru Akagi_
