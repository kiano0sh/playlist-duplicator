import bs4 as bs
import subprocess
from urllib.parse import unquote
from html import unescape

xml_location = str(input("Please enter your xspf location: "))
playlist_name = str(input("Please choose a name for your playlist: "))


def get_addresses():
    with open(xml_location, 'r') as x:
        x = x.read()
        soup = bs.BeautifulSoup(x, 'xml')
        locations = [loc.text for loc in soup.find_all('location')]
        locations = [(unescape(unquote(l[7:]))) for l in locations]
        return locations


def copy_files():
    locations = get_addresses()
    subprocess.call(['mkdir', '{}'.format(playlist_name)])
    for loc in locations:
        subprocess.check_output(['sudo', 'cp', loc, './{}/'.format(playlist_name)])


if __name__ == '__main__':
    copy_files()
