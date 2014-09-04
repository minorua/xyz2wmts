#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import settings
print json.dumps({"service": settings.service, "layers": settings.layers}, sort_keys=False, indent=2)
