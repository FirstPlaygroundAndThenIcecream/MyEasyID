from flask import Flask
import json, xmltodict
# import dataFormatConverter

app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h1>Bank Server!</h1>

    <iframe src="https://w3certified.com/easyid/easyid-form.php" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """

o = xmltodict.parse('<person> <first>John</first> <last>Johnsen</last> <country>Denmark</country> </person>')
x = json.dumps(o) 

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


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj._dict_

y = json.dumps(x, default=dumper, indent=2)
loaded_y = json.loads(y)

# person_dict = dataFormatConverter.xml_2_json('xml_data.xml')


@app.route('/test-JSON-print')
def testJS0N():
    return '''{"all": 
                {"person": 
                    [{
                        "@register": "2000", 
                        "@title": "student", 
                        "name": 
                        {
                            "first": "John", 
                            "last": "Johnsen"
                        }, 
                        "country": "Denmark"
                    }, {
                        "@register": "2000", 
                        "@title": "teacher", 
                        "name": 
                        {
                            "first": "Peter", 
                            "last": "Petersen"
                            }, 
                        "country": "Norway"
                    }]
                }
            }'''




if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)