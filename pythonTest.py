thisDict = {
    "name": "John",
    "attributes": {
        "register": "2000",
        "identity": "student"
    },
    "country": "denmark"
}

person_json_str ={'all': 
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

# print(thisDict["attributes"]["register"][0])

print(person_json_str['all']['person'][0])
print(person_json_str['all']['person'][1])