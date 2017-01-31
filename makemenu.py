# -*- coding: utf-8 -*-

import json
from sys import argv

for section in json.load(open(argv[1])):
    print('\\section*{%s}\\begin{tabular}{rl}' % section['category'])
    for item in section['content']:
        print(u'%s & %.2f\\euro\\\\' % (item['name'], item['price']))
    print('\\end{tabular}')
