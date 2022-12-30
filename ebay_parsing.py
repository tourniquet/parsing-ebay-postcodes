from bs4 import BeautifulSoup

with open('ebay.html', 'r') as file_object:
  doc = BeautifulSoup(file_object, 'html.parser')
  postcodes = doc.find_all('span', class_='zip-code')

with open('postcodes.txt', 'w') as file_object:
  for postcode in postcodes:
    file_object.write(postcode.string.upper() + ',\n')
