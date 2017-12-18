#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def outputline(line, num_columns):
    c = line.count('\t')
    text = line.replace('\t', '|')
    print('|' + text + ('|' * (num_columns-c)))

### Initialize

lines = os.environ['POPCLIP_TEXT'].splitlines()

# If option key(⌥) is pressed, treat the first line as a header
modified = 1 if (os.environ['POPCLIP_MODIFIER_FLAGS'] == "524288") else 0

# Count the maximum number of columns in each row
num_columns = reduce(lambda x,y: max(x, y), map(lambda l: l.count('\t'), lines)) + 1

### Convert & Output

# Header
if modified:
    outputline(lines[0], num_columns)
    lines = lines[1:]
else:
	print('|' * (num_columns) + '|')

# Separator
print '|---' * (num_columns) + '|'

# Contents
for line in lines:
    outputline(line, num_columns)
