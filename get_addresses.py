import xml.etree.ElementTree as et
import urllib2
from BeautifulSoup import BeautifulSoup

def get_address_from_item(itemguid):
  # load page
  response = urllib2.urlopen(itemguid)
  content = response.read()
  response.close()

  soup = BeautifulSoup(content)
  # so boring of me
  return soup.find(id='MapLink').parent.contents[0].string

def parse_rss():
    tree = et.parse('trucks.rss') # TODO
    root = tree.getroot()

    # rss
    #   channel
    #     title
    #     link
    #     description
    #     blah blah blah
    #     ITEM
    #       title
    #       link
    #       blah blah blah
    #       guid (same as link?)

    for car in root.find('channel').findall('item'):
      title = car.find('title').text
      guid = car.find('guid').text
      print title, guid, get_address_from_item(guid)

if __name__ == '__main__':
    parse_rss()
