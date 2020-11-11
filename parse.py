#!/usr/bin/env python3
#sed 's/Steam//' source.txt | sed 's/  /|/' | sed 's/http.*=//' > list.txt
from os.path import expanduser
import re
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

regex = '^.*{}.*$'

output_mods = ""
not_found = []

with open(expanduser('~/modlists/allmods.txt'), 'r') as all_mods_file:
    allmods = all_mods_file.read()

with open(expanduser(args.input), 'r') as f:
    for line in f:
        name, id = map(str.strip, line.split('|'))
        match = re.findall(regex.format(id), allmods, re.MULTILINE)
        if match:
            output_mods += match[0] + '\n'
        else:
            not_found.append([name, id])
            name = name.lower()
            name = re.sub('\(.*\)', '', name).strip()
            name = name.replace(' ', '_')
            output_mods += "@{} {}\n".format(name, id)

with open(expanduser(args.output), 'w') as f:
    f.write(output_mods)
