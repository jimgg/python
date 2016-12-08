#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import json
import os
import subprocess
import uuid

tpl = """
digraph g {
size="50,50"
node[shape=record,style=filled,fillcolor=gray95]
edge[dir=back, arrowtail=vee]

%s
}
"""


def gen_png(data, out_file):
    file_name = os.path.join(os.path.dirname(__file__), str(uuid.uuid4()))
    with open(file_name, 'w') as f:
        f.write(data)
    cmd = ['dot', file_name, '-Tpng', '-o', out_file]
    subprocess.call(cmd)
    os.remove(file_name)


def gen_data(file_name):
    with open(file_name) as f:
        data = json.loads(f.read())
    res = []
    for class_name, fields in data['nodes'].iteritems():
        cf = ['%s\l' % field for field in fields]
        # cf = []
        # for field in fields:
        #     if field[0] in ('#', '+', '-'):
        #         field = '%s\l' % field
        #     else:
        #         field = '+ %s\l' % field
        #     cf.append(field)
        res.append('{class_name}[label="{{{class_name}|{fields}}}"]'.format(class_name=class_name, fields=''.join(cf)))
    for edge in data['edges']:
        res.append(edge)
    data = tpl % '\n'.join(res)
    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate uml class diagram')
    parser.add_argument('file')
    parser.add_argument('-o', '--output', dest='output', help='output file', action='store')
    args = parser.parse_args()
    gen_png(gen_data(args.file), args.output)
