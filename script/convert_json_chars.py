#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json

data = sys.stdin.read()
sys.stdout.write(json.dumps(json.loads(data), ensure_ascii=False).encode('utf8'))
