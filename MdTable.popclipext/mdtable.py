#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import csv
import StringIO

reload(sys)
sys.setdefaultencoding('utf-8')

def outputline(columns, maxnum_columns):
    c = len(columns)
    columns = map(lambda t: t.replace('\n','<br/>'), columns)
    text = '|'.join(columns)
    print('|' + text + ('|' * (maxnum_columns-c))) + '|'

### Initialize

# If option key(⌥) is pressed, treat the first line as a header
modified = 1 if (os.environ['POPCLIP_MODIFIER_FLAGS'] == "524288") else 0

# Get whole text
# input = ""
# for line in sys.stdin:
# 	input += line + '\n'
input = os.environ['POPCLIP_TEXT']
io = StringIO.StringIO(input)

# Guess the dialect
try:
    dialect = csv.Sniffer().sniff(io.readline(), "\t,")
except:
    dialect = csv.excel
io.seek(0)

# Convert text to a list of rows
rows = []
for row in csv.reader(io, dialect):
    rows.append(row)

# Count the maximum number of columns in each row
maxnum_columns = reduce(lambda x,y: max(x, y), map(lambda row: len(row), rows))

### Convert & Output

# Header
if modified:
    outputline(rows[0], maxnum_columns)
    rows = rows[1:]
else:
	print('|' * (maxnum_columns) + '|')

# Separator
print '|---' * (maxnum_columns) + '|'

# Contents
for columns in rows:
    outputline(columns, maxnum_columns)
