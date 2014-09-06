#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from xyz2wmts import WMTSLayerDef

def settings2dict(settings):
  d = {}
  d["metadataURL"] = settings.metadataURL
  if hasattr(settings, "service"):
    d["service"] = settings.service
  if hasattr(settings, "provider"):
    d["provider"] = settings.provider
  d["layers"] = []
  for layer in settings.layers:
    if isinstance(layer, dict):
      d["layers"].append(layer)
    else:
      ld = {}
      for i, v in enumerate(layer):
        ld[WMTSLayerDef.PARAMS[i]] = v
      d["layers"].append(ld)
  return d

import settings
print json.dumps(settings2dict(settings), ensure_ascii=False, sort_keys=False, indent=2)
