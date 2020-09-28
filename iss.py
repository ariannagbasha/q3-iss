#!/usr/bin/env python

__author__ = 'ariannagbasha a.k.a Gabby collabs: Shanquel and Sondos'

import requests

def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json').json()
    num_peeps = r['number']
    who_peeps = 'People: '
    for astros in r['people']:
        who_peeps += astros['name'] + ' , '
    print(f'Number of people in the station: {num_peeps}')
    print(who_peeps)


def coordinates():
    r = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat = r['iss_position']['latitude']
    lon = r['iss_position']['longitude']
    print(f'Iss Position: {lat} {lon}')
    return [lon, lat]


def main():
    astronauts()


if __name__ == '__main__':
    main()
