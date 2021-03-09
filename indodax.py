#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
indodax.py: A polybar script that displays the price of crypto-currencies.
Forked from https://github.com/willHol/polybar-crypto to suit with Indodax API.
"""

__author__ = "Christian Dita Putratama"
__copyright__ = "Copyright 2021, Christian Dita Putratama"
__credits__ = ["willHol"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Christian Dita Putratama"
__email__ = "ditatompel@gmail.com"
__status__ = "Development"

import sys, locale, configparser
from requests import get
from pathlib import Path

locale.setlocale(locale.LC_ALL, '') # Use '' for auto, or force e.g. to 'en_US.UTF-8
config = configparser.ConfigParser()

# File must be opened with utf-8 explicitly
with open(Path(__file__).parent / "config", 'r', encoding='utf-8') as f:
    config.read_file(f)

# Everything except the general section
pairs = [x for x in config.sections() if x != 'general']
display_opt = config['general']['display']
color_symbol = config['general']['color_symbol']
color_down = config['general']['color_down']
color_up = config['general']['color_up']

json = get(f'https://indodax.com/api/summaries').json()
for currency in pairs:
    symbol = config[currency]['symbol']
    if currency in json['tickers']:
        last = int(json['tickers'][currency]['last'])
        price_24 = int(json['prices_24h'][currency.replace('_', '')])
        if last < price_24:
            change24 = ('%{F' + color_down + '}-' +
                        str(round(((price_24 - last) / last) * 100, 2)) +
                        '%%{F-}')
        elif last > price_24:
            change24 = ('%{F' + color_up + '}+' +
                        str(round(((last - price_24) / price_24) * 100, 2)) +
                        '%%{F-}')
        else:
            change24 = '0%'
        if display_opt == 'percentage':
            sys.stdout.write(f'%{{F{color_symbol}}}{symbol}%{{F-}}: {change24}  ')
        elif display_opt == 'price':
            sys.stdout.write(f'%{{F{color_symbol}}}{symbol}%{{F-}}: {last:n}  ')
        else:
            sys.stdout.write(f'%{{F{color_symbol}}}{symbol}%{{F-}}: {last:n}/{change24}  ')
