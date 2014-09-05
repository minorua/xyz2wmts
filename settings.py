#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ================================
#            Settings
# ================================

# WMTS service
service = {"Title": "Title",
           "Abstract": {"en": "Abstract"},
           "Keywords": ["Keyword"],
           "Fees": "",
           "AccessConstraints": "",
           "ServiceMetadataURL": "http://localhost/wmts/1.0.0/WMTSCapabilities.xml"}

# WMTS layer

# Layer definition formats
#  1. list:
#   [identifier as unicode, title as unicode, abstract as unicode, templateUrl as str,
#    zmin as int, zmax as int, bbox in WGS84 as list [xmin, ymin, xmax, ymax], format as str]
#
#   - identifier, title, abstract and templateUrl are mandatory.

#  2. dict:
#   {"identifier": u"id", "title": u"title", "abstract": u"abstract",
#    "templateUrl": "http://localhost/wmts/layer/{z}/{x}/{y}.png",
#    "zmin": 0, "zmax": 18, "bbox": [xmin, ymin, xmax, ymax], "format": "image/png"}
#
#   - identifier, title and templateUrl are mandatory.
#
#  in common:
#   - {z}, {x} and {y} in templateUrl will be replaced with {TileMatrix}, {TileCol} and {TileRow}.
#   - format is detected from templateUrl if not specified.

layers = []

# TODO: remove the following and write your own definitions


# Layer definition examples
# - Worldwide
layers.append([u"osm", u"OpenStreetMap", u"", "http://localhost/wmts/osm/{z}/{x}/{y}.png", 0, 19])
layers.append({"identifier": u"osm_2", "title": u"OpenStreetMap 2",
               "templateUrl": "http://localhost/wmts/osm/{z}/{x}/{y}.png", "zmin": 0, "zmax": 19})

# - Regional map
layers.append([u"srtm3_shaded_relief", u"SRTM3 SHADED RELIEF (JAPAN)", u"The source is SRTM3.",
               "http://localhost/wmts/srtm3_shaded_relief/{z}/{x}/{y}.png",
               3, 10, [119.9995833, 19.9995833, 154.0004167, 47.0004167]])
layers.append({"identifier": u"srtm3_shaded_relief_2",
               "title": u"SRTM3 SHADED RELIEF (JAPAN) 2",
               "abstract": u"The source is SRTM3.", 
               "templateUrl": "http://localhost/wmts/srtm3_shaded_relief/{z}/{x}/{y}.png",
               "zmin": 3, "zmax": 10, "bbox": [119.9995833, 19.9995833, 154.0004167, 47.0004167]})
