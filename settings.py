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
           "ServiceMetadataURL": "http://localhost/WMTSCapabilities.xml"}

# WMTS layer
# Layer definition formats
#  1. list:
#   [identifier as unicode, title as unicode, templateUrl as str, abstract as unicode,
#    zmin as int, zmax as int, bbox in WGS84 as list [xmin, ymin, xmax, ymax], format as str]
#  2. dict:
#   {"identifier": u"id", "title": u"title",
#    "templateUrl": "http://localhost/wmts/layer1/{z}/{x}/{y}.png", "abstract": u"abstract",
#    "zmin": 0, "zmax": 18, "bbox": [xmin, ymin, xmax, ymax], "format": "image/png"}
#
# identifier, title and templateUrl are mandatory.
# {z}, {x} and {y} in templateUrl will be replaced with {TileMatrix}, {TileCol} and {TileRow}.
# format is detected from templateUrl if not specified.

layers = []

# TODO: remove the following and write your own definitions

# layer definition examples
layers.append([u"srtm3_shaded_relief", u"SRTM3 SHADED RELIEF (JAPAN)", "http://localhost/wmts/srtm3_shaded_relief/{z}/{x}/{y}.png", u"The source is SRTM3.", 3, 10, [119.9995833, 19.9995833, 154.0004167, 47.0004167]])
layers.append({"identifier": u"srtm3_shaded_relief_2", "title": u"SRTM3 SHADED RELIEF (JAPAN) 2", "templateUrl": "http://localhost/wmts/srtm3_shaded_relief/{z}/{x}/{y}.png", "abstract": u"The source is SRTM3.", "zmin": 3, "zmax": 10, "bbox": [119.9995833, 19.9995833, 154.0004167, 47.0004167]})
