#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flags

from .api import Wialon, WialonError
# Silence potential warnings from static analysis tools:
assert Wialon
assert WialonError

__author__ = "Alex Chernetsky chal@gurtam.com"
__copyright__ = ("Copyright 2013, Gurtam; ",)

__credits__ = ["Alex Chernetsky", ]
__version__ = "1.0.1"

__all__ = ["Wialon"]
