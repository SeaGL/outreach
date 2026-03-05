#!/usr/bin/env python

import segno

qr = segno.make('https://seagl.org', error='h')
qr.to_artistic(background='website-sticker.svg', target='website-qr.png', scale=25)

qr = segno.make('https://seagl.org/links', error='h')
qr.to_artistic(background='links-sticker.svg', target='links-qr.png', scale=25)
