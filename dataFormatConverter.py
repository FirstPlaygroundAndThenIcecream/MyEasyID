import xmltodict, json, pprint, csv, sys
from json2xml import json2xml, readfromurl, readfromstring, readfromjson
import xml.etree.ElementTree as ET

person_xml_str = '<person> <first>John</first> <last>Johnsen</last> <country>Denmark</country> </person>'

person_json_dict ={'all': 
                    {'person': 
                        [{'@register': '2000', '@title': 'student', 
                            'name': 
                            {
                                'first': 'John', 
                                'last': 'Johnsen'
                            }, 
                            'country': 'Denmark'
                            }, 
                            {'@register': '2000', '@title': 'teacher', 
                            'name': 
                            {
                                'first': 'Peter', 
                                'last': 'Petersen'
                            }, 
                            'country': 'Norway'
                        }]
                    }
                }

# # xml to json, csv

# xml to json 
def xml_2_json(fileName):
  with open(fileName) as fd:
    person_orderedDict = xmltodict.parse(fd.read())
  # person_orderedDict = xmltodict.parse(person_xml)             # here can parse a xml str 
  person_str = json.dumps(person_orderedDict)                    # change from orderedDict to str, as it is a format the loads method can accept
  print(person_str)
  person_json = json.loads(person_str)
  return person_json

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
   
#####################################################################

# # json to xml

# json to xml, get data from a str
def json_2_xml_str(dataStr):
  data = readfromstring(dataStr)
  data_xml = json2xml.Json2xml(data).to_xml()
  print(data_xml)

# json to xml, get data from a url
def json_2_xml_url(url):
  data_fromUrl = readfromurl(url)
  data_fromUrl_xml = json2xml.Json2xml(data_fromUrl).to_xml()
  print(data_fromUrl_xml)

# json to xml, get data from json file
def json_2_xml_jsonfile(jsonFileName):
  data_txt = readfromjson(jsonFileName)
  data_txt_xml = json2xml.Json2xml(data_txt).to_xml()
  print(data_txt_xml)

# json to csv
def json_2_csv():
  fileInput = sys.argv[1]
  fileOutput = sys.argv[2]    
  
  inputFile = open(fileInput) #open json file
  outputFile = open(fileOutput, 'w') #load csv file
  data = json.load(inputFile) #load json content
  inputFile.close() #close the input file    output = csv.writer(outputFile) #create a csv.write    output.writerow(data[0].keys())  # header row    for row in data:
  output.writerow(row.values()) #values row

#####################################################################

# xml_file = 'xml_data.xml'
# xml_2_csv(xml_file)
# print(xml_2_json(xml_file))

# json_str = '{"first": "John", "last": "Johnsen", "country": "Denmark"}'
# json_2_xml_str(json_str)

# json_url = "http://127.0.0.1:5000/test-JSON-print"
# json_2_xml_url(json_url)

json_file = "./JSON_data.json"
json_2_xml_jsonfile(json_file)