import xmltodict, json, pprint, csv, sys
from json2xml import json2xml, readfromurl, readfromstring, readfromjson
import xml.etree.ElementTree as ET

########################################
##          xml to json, csv          ##
########################################

# xml to json 
def xml_2_json(fileName):
  with open(fileName) as f:
    person_orderedDict = xmltodict.parse(f.read())                # here can parse a xml str 
  person_json = json.dumps(person_orderedDict)                    # change from orderedDict to str, as it is a format the loads method can accept
  # person_dict = json.loads(person_json)
  return person_json

xml_file = 'xml_data.xml'
print(xml_2_json(xml_file))


# xml to csv
def xml_2_csv(fileName):
  tree = ET.parse(fileName)
  root = tree.getroot()                                          # ET.tostring(root, encoding='utf8').decode('utf8') - this prints out the whole xml file
                   
  for child in root:
    print(child.tag, child.attrib)

  for child in root.find('./person/name'):                           # return tags under name by using Xpath
    print(child.tag)

  for elem in root.findall("./person/[@register='2000']"):           # return all person atrributes with attribute register=2000
    print(elem.attrib)

  f = open('xml2csv.csv', 'w+', newline='\n')
  csvWriter = csv.writer(f)

  head = ['first_name', 'last_name', 'country', '@register_year', '@title']
  csvWriter.writerow(head)

  for person in root.iter('person'):
    row = []
    first_name = person.find('name').find('first').text
    row.append(first_name)
    last_name = person.find('name').find('last').text
    row.append(last_name)
    country = person.find('country').text
    row.append(country)
    register = (person.attrib['register'])
    row.append(register)
    title = (person.attrib['title'])
    row.append(title)
    csvWriter.writerow(row)
    print('row: ' + str(row))

  f.close()

# xml_2_csv(xml_file)



########################################
##          json to xml, csv          ##
########################################

# json to xml, get data from a str
def json_2_xml_str(dataStr):
  try:
    data = readfromstring(dataStr)
    data_xml = json2xml.Json2xml(data).to_xml()
    print(data_xml)
  except:
   print("an error occured")

# json_str = '{"first": "John", "last": "Johnsen", "country": "Denmark"}'
# json_2_xml_str(json_str)


# json to xml, get data from a url
def json_2_xml_url(url):
  data_fromUrl = readfromurl(url)
  data_fromUrl_xml = json2xml.Json2xml(data_fromUrl).to_xml()
  print(data_fromUrl_xml)

# json_url = "http://127.0.0.1:5000/test-JSON-print"
# json_2_xml_url(json_url)


# json to xml, get data from json file
def json_2_xml_jsonfile(jsonFileName):
  data_txt = readfromjson(jsonFileName)
  data_txt_xml = json2xml.Json2xml(data_txt).to_xml()
  print(data_txt_xml)

# json_file = "./JSON_data.json"
# json_2_xml_jsonfile(json_file)


# json to csv
def json_2_csv():
  with open('JSON_data.json') as json_file:
    data = json.load(json_file)

    data_person = data['all']['person']
    print(data_person)

  csv_file = open('json_2_csv.txt', 'w+', newline='\n')
  csvWriter = csv.writer(csv_file)

  header = ['@register', '@title', 'firstName', 'lastName', 'Country']
  csvWriter.writerow(header)

  for person in data_person:
    row = []
    row.append(person['@register'])
    row.append(person['@title'])
    row.append(person['name']['first'])
    row.append(person['name']['last'])
    row.append(person['country'])
    csvWriter.writerow(row)
  
  csv_file.close()

#json_2_csv()



########################################
##          csv to json, xml          ##
########################################


# csv to json
def csv_2_json():
  csvFilePath = 'xml2csv.csv'
  jsonFilePath = 'csv_2_json.json'

  data = {}
  with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:    #row is orderedDict
      data.setdefault('person', [])
      data['person'].append(row)
    print(json.dumps(data, indent=4))
  
  with open(jsonFilePath, 'a', newline='\n') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

# csv_2_json()


# csv to xml
def csv_2_xml():
  csvFilePath = 'xml2csv.csv'
  xmlFilePath = 'csv_2_xml.xml'

  data = []
  with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:    #row is orderedDict
      data.append(row)
  print(len(data))
  for i in range(0, 2):
    print(data[i])
  # print(data[0])

  with open(xmlFilePath, 'w+', newline='\n') as xmlWriter:
    xmlWriter.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xmlWriter.write('<all>\n')
    for i in range(0, len(data)):
      xmlWriter.write('   ' + '<person register="' + data[i]['@register_year'] + '" title="' + data[i]['@title'] + '">\n')
      xmlWriter.write('       ' + '<first_name>' + data[i]['first_name'] + '</first_name>\n')
      xmlWriter.write('       ' + '<last_name>' + data[i]['last_name'] + '</last_name>\n')
      xmlWriter.write('       ' + '<country>' + data[i]['country'] + '</country>\n')
      xmlWriter.write('   ' + '</person>\n')
    xmlWriter.write('</all>\n')

# csv_2_xml()