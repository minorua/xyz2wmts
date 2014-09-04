#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project   : Simple WCS Server
# begin     : 2014-07-26
# copyright : (C) 2014 Minoru Akagi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import xml.dom.minidom

class MyXMLDocument:
  def __init__(self):
    self._doc = xml.dom.minidom.Document()

  def append(self, parent, tagName, attributes=None, text=""):
    elem = self._doc.createElement(tagName)
    for key, value in (attributes or {}).iteritems():
      elem.setAttribute(key, value)
    if text:
      elem.appendChild(self._doc.createTextNode(text))
    return (parent or self._doc).appendChild(elem)

  def appendTree(self, parent, dictionary):
    for k, v in dictionary.iteritems():
      if isinstance(v, dict):
        self.appendTree(self.append(parent, k), v)
      else:
        self.append(parent, k, text=str(v))

  def document(self):
    return self._doc
