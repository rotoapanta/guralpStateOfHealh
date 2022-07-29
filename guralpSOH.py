#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
__file__ = guralpStateOfHealh.py
__author__ = rotoapanta "Roberto Toapanta"
__copyright__ = "Copyright 2021, BitTech"
__credits__ = ["Roberto Toapanta, Giovanny Toapanta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roberto Toapanta"
__email__ = "robertocarlos.toapanta@gmail.com"
__status__ = "Production"
__date__ = 30/6/22 20:59
__description__ = " "
__information__ : Python3 code to demonstrate
                  Getting date and time values in ISO 8601 format
                 https://curlconverter.com/
"""

import requests
from requests.auth import HTTPDigestAuth
import datetime

# IP_EQUIPMENT = '192.168.XXX.XX'
IP_EQUIPMENT = '192.168.XXX.XX'
# hola

todays_Date = datetime.datetime.now()  # Getting today's date and time
DateTime_in_ISOFormat = todays_Date.isoformat()  # Calling the isoformat() function over the today's date and time
print("Today's date and time in ISO Format: %s" % DateTime_in_ISOFormat)  # Printing Today's date and time in ISO format

files = [
    ('output', (None, 'text')),
    ('start', (None, DateTime_in_ISOFormat)),
    ('end', (None, DateTime_in_ISOFormat)),
    ('value', (None, 'Sensor_power/current')),
    ('value', (None, 'Sensor_power/voltage')),
    ('value', (None, 'system_temperature/temp')),
    ('action', (None, 'Get data')),
]

response = requests.post('http://' + IP_EQUIPMENT + '/cgi-bin.auth/envirolog.cgi', files=files,
                         auth=HTTPDigestAuth('root', 'renacig'))

with open('CIVI.txt', 'wb') as f:
    f.write(response.content)

# NOMBRE_ARCHIVO = '/home/rotoapanta/PycharmProjects/guralpData/CIVI.txt'
NOMBRE_ARCHIVO = '/Users/rotoapanta/Library/CloudStorage/OneDrive-Personal/RC_AG_Documents/Projects/Zabbix/guralpStateOfHealh/CIVI.txt'


def print_data():
    fichero = open(NOMBRE_ARCHIVO)

    for numero, linea in enumerate(fichero):
        if numero == 3:  # Segunda línea, pues la primera sería la numero 0
            a = linea.split()
            print(a[2])  # voltage data
            print(a[3])  # temperature data
            break
    fichero.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_data()
