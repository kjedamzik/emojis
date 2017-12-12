#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from base64 import b64decode
from csv import writer
from os import makedirs, path
from errno import EEXIST


def parse(filename):
    with open(filename) as f:
        html_doc = f.read()
    return BeautifulSoup(html_doc, 'html.parser')


def write_base64(f, s):
    if not s:
        return

    try:
        makedirs(path.dirname(f))
    except OSError as exception:
        if exception.errno != EEXIST:
            raise

    with open(f, 'wb') as f:
        f.write(b64decode(s))


def img_src(n):
    try:
        return n.img['src'].split(',')[1]
    except:
        return None


def get_emojilist(html):
    emojis = list()
    for row in html.find('table').find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 15:
            emojis.append(dict(no=cols[0].text.strip(),
                               code=cols[1].text.strip(),
                               browser=cols[2].text.strip(),
                               apple=img_src(cols[3]),
                               google=img_src(cols[4]),
                               twitter=img_src(cols[5]),
                               one=img_src(cols[6])))
    return emojis


def write_images(emojilist):
    for emoji in emojilist:
        for m in ['apple', 'google', 'twitter', 'one']:
            write_base64("./images/{}/{}.png".format(m, emoji['code'].replace('U+', '').replace(' ', '_').lower()), emoji[m])


def write_csv(emojilist):
    with open('emojis.csv', 'w') as csvfile:
        w = writer(csvfile)
        w.writerow(['no', 'codepoints', 'filename', 'emoji'])

        for emoji in emojilist:
            w.writerow([emoji['no'],
                        ''.join('\\u{{{}}}'.format(x) for x in emoji['code'].replace('U+', '').split(' ')).lower(),
                        emoji['code'].replace('U+', '').replace(' ', '_').lower() + '.png',
                        emoji['browser']])


if __name__ == "__main__":
    html = parse("full-emoji-list.html")

    el = get_emojilist(html)

    write_images(el)

    write_csv(el)
