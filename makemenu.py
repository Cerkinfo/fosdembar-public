# -*- coding: utf-8 -*-

import json
from sys import argv

for section in json.load(open(argv[1])):
    print('\\section*{%s}\\begin{tabular}{rl}' % section['category'])
    for item in section['content']:
        print(u'%s%s & %.2f\\euro\\\\' % (item['name'], (" (%s\degree)" % item['alcool']) if 'alcool' in item else '', item['price']))
    print('\\end{tabular}')
