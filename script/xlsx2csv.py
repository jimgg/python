# -*- coding: utf8 -*-

import sys
from openpyxl import load_workbook

file_name = sys.argv[1]
wb = load_workbook(file_name)
ws = wb.active

for row in ws.rows:
    items = []
    if not row:
        continue
    for cell in row:
        if cell:
            value = cell.value and cell.value or ''
        else:
            value = ''
        items.append(value.replace('\n', ','))
    if items[0]:
        print ';'.join(items).encode('utf8')
