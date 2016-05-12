#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flags

from .api import Wialon, WialonError
# Silence potential warnings from static analysis tools:
assert Wialon
assert WialonError

__author__ = "Alex Chernetsky chal@gurtam.com"
__copyright__ = ("Copyright 2013-2016, Gurtam; ",)

__credits__ = ["Alex Chernetsky", "Aleksey Shmigelski"]
__version__ = "1.1.0"

__all__ = ["Wialon"]
