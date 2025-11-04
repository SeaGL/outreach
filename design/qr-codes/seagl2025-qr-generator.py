#!/usr/bin/env python

import segno

qr = segno.make('https://seagl.org/schedule', error='h')
qr.to_artistic(background='schedule-qr-sticker.svg', target='schedule-qr.png', scale=25)

qr = segno.make('https://seagl.org/feedback', error='h')
qr.to_artistic(background='feedback-qr-sticker.svg', target='feedback-qr.png', scale=25)

#qr = segno.make('https://seagl.org/wifi', error='h')
qr = segno.make('WIFI:T:nopass;S:University of Washington;P:;H:false;;', error='h')
qr.to_artistic(background='wifi-qr-sticker.svg', target='wifi-qr.png', scale=25)

qr = segno.make('https://seagl.org/teagl', error='h')
qr.to_artistic(background='teagl-qr-sticker.svg', target='teagl-qr.png', scale=25)

qr = segno.make('https://seagl.org/register', error='h')
qr.to_artistic(background='registration-qr-sticker.svg', target='registration-qr.png', scale=25)

qr = segno.make('https://seagl.org/donate', error='h')
qr.to_artistic(background='donation-qr-sticker.svg', target='donation-qr.png', scale=25)

qr = segno.make('https://seagl.org/cfp', error='h')
qr.to_artistic(background='cfp-qr-sticker.svg', target='cfp-qr.png', scale=25)
