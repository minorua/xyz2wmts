# xyz2wmts - version beta
xyz2wmts helps you to start providing [OGC WMTS](http://www.opengeospatial.org/standards/wmts) by generating service metadata.

## How to use?
 1. generate XYZ tiles using a tile generator such as [MapTiler](http://www.maptiler.org/).
 2. edit service metadata in `settings.py` and add your layer definitions into it.
 3. run `python xyz2wmts.py > WMTSCapabilities.xml`.
 4. upload tiles and WMTSCapabilities.xml to a web server.

**See OGC Documents for details of WMTS and WMTSCapabilities.xml**
 * [Web Map Tile Service Implementation Standard](http://www.opengeospatial.org/standards/wmts)
 * [Web Service Common Implementation Specification](http://www.opengeospatial.org/standards/common)

## Sample WMTS

Metadata URL is https://dl.dropboxusercontent.com/u/21526091/wmts/1.0.0/WMTSCapabilities.xml

Layer

* SRTM3 SHADED RELIEF (JAPAN) - Shaded relief map made from SRTM-3 data

## License
MIT License

_Copyright (c) 2014, Minoru Akagi_
