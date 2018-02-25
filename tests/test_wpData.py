from wp_iso3166 import countries
import os


def iso3_name():
    f = os.path.dirname(__file__)
    f = os.path.join(f, __file__[:-3], 'wp_isos.csv')
    with open(f, 'rb') as file:
        line = file.readline()
        while line != b'':
            yield line.strip().decode().replace('"', '').split(',', maxsplit=1)
            line = file.readline()


def test_wpdata():
    for iso3, name in iso3_name():
        c = countries.get(iso3)
        assert c.name == name
