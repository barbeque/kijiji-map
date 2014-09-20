import xml.etree.ElementTree as et

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
  print title, guid
