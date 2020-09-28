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

def main():
    astronauts()


if __name__ == '__main__':
    main()
