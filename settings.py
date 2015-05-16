#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ================================
#            Settings
# ================================

# WMTS metadata URL
metadataURL = "https://gist.githubusercontent.com/minorua/1f047985f87597030dce/raw/WMTSCapabilities.xml"

# WMTS
service = {"Title": u"地理院タイル(WMTSテスト)",
           "Abstract": {"ja": u"このサービスは国土地理院の地理院タイルをWMTSクライアントから利用可能にします。こうしたWMTSメタデータ(XML文書)は第三者が公開するべきではないと思われますが、QGISからのWMTS利用の試験用として暫時公開します。地理院タイルの利用にあたっては地理院タイル利用規約(http://portal.cyberjapan.jp/help/termsofuse.html)に従って下さい。"},
           "Keywords": [],
           "Fees": "",                      # NONE if no fees or terms
           "AccessConstraints": ""}         # NONE if no constraint


# WMTS provider
provider = {"Name": "ProviderName",
            "SiteURL": "http://localhost/"}
provider = {}                              # uncomment if provider information is not necessary


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

layers.append(["std",u"標準地図","","http://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png",2,18])
layers.append(["pale",u"淡色地図","","http://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png",12,18,[122.78,20.4,154.78,45.58]])
layers.append(["blank",u"白地図","","http://cyberjapandata.gsi.go.jp/xyz/blank/{z}/{x}/{y}.png",5,14,[122.78,20.4,154.78,45.58]])
layers.append(["english","English","","http://cyberjapandata.gsi.go.jp/xyz/english/{z}/{x}/{y}.png",5,11,[122.78,20.4,154.78,45.58]])
layers.append(["relief",u"色別標高図","","http://cyberjapandata.gsi.go.jp/xyz/relief/{z}/{x}/{y}.png",5,15,[122.78,20.4,154.78,45.58]])
layers.append(["ort",u"写真","","http://cyberjapandata.gsi.go.jp/xyz/ort/{z}/{x}/{y}.jpg",2,17])
layers.append(["gazo1",u"国土画像情報（第一期：1974～1978年撮影）","","http://cyberjapandata.gsi.go.jp/xyz/gazo1/{z}/{x}/{y}.jpg",10,17,[122.78,20.4,154.78,45.58]])
layers.append(["gazo2",u"国土画像情報（第二期：1979～1983年撮影）","","http://cyberjapandata.gsi.go.jp/xyz/gazo2/{z}/{x}/{y}.jpg",15,17,[122.78,20.4,154.78,45.58]])
layers.append(["gazo3",u"国土画像情報（第三期：1984～1986年撮影）","","http://cyberjapandata.gsi.go.jp/xyz/gazo3/{z}/{x}/{y}.jpg",15,17,[122.78,20.4,154.78,45.58]])
layers.append(["gazo4",u"国土画像情報（第四期：1988～1990年撮影）","","http://cyberjapandata.gsi.go.jp/xyz/gazo4/{z}/{x}/{y}.jpg",15,17,[122.78,20.4,154.78,45.58]])
layers.append(["ort_old10",u"空中写真（1961～1964年）","","http://cyberjapandata.gsi.go.jp/xyz/ort_old10/{z}/{x}/{y}.png",15,17,[122.78,20.4,154.78,45.58]])
layers.append(["ort_USA10",u"空中写真（1945～1950年）","","http://cyberjapandata.gsi.go.jp/xyz/ort_USA10/{z}/{x}/{y}.png",15,17,[122.78,20.4,154.78,45.58]])
layers.append(["airphoto",u"簡易空中写真（2004年～）","","http://cyberjapandata.gsi.go.jp/xyz/airphoto/{z}/{x}/{y}.png",5,18,[122.78,20.4,154.78,45.58]])
