import pickle

# declare a dict
myDict = {"first_name":"John"}

# different ways of adding key-value pair
myDict["last_name"] = "Johnny"

myDict.update({"country":"denmark"})

myDict["interests"] = ["a", "b", "c"]

myDict["interests"].append('d')

# # return the value and remove from the dict
# last_name = myDict.pop("last_name")

# access value
first_name = myDict['first_name']

# # delete key-value pair or the whole dict
# del myDict['country']
# del myDict

# # clear the content of a dict
# myDict.clear()

for key, value in myDict.items():
    print (key, value)

for i in myDict["interests"]:
    print (i)


serial_myDict = pickle.dumps(myDict)
print(serial_myDict)

received_myDict = pickle.loads(serial_myDict)
print(received_myDict)
