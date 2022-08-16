#!/usr/bin/env python3
import argparse
from os.path import expanduser
import re

from bs4 import BeautifulSoup

def main(filename):
    regex_id = 'http.*=(.*)'
    regex_modline = '^.*{}.*$'

    output_mods = ""
    not_found = []

    with open(expanduser('~/modlists/allmods.txt'), 'r') as f:
        allmods = f.read()

    with open(filename) as f:
        html = f.read()

    soup = BeautifulSoup(html, features='html.parser')
    mods = soup.select('[data-type="ModContainer"]')
    for mod in mods:
        name, url = [x.string
                     for x in
                     mod.select('[data-type="DisplayName"], '
                                '[data-type="Link"]')]
        name = (name
                .replace(':', '')
                .replace('\'', '')
                .replace('-', '')
                .replace('  ', ' ')
               )
        mod_id = re.match(regex_id, url).group(1)
        match = re.findall(regex_modline.format(mod_id), allmods, re.MULTILINE)

        if match:
            output_mods += match[0] + '\n'
        else:
            not_found.append([name, mod_id])
            name = name.lower()
            name = re.sub('\(.*\)', '', name).strip()
            name = name.replace(' ', '_')
            output_mods += "@{} {}\n".format(name, mod_id)
    print(output_mods.strip())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parse modlists from HTML")
    parser.add_argument('file', help="HTML file")

    args = parser.parse_args()
    main(args.file)
