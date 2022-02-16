#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"}
]
sports_directory = {
    "basketball" : ["Kobe", "Jordan", "James", "Curry"],
    "soccer" : ["Messi", "Ronaldo", "Rooney"]
}
z = [ {"x": 10, "y": 20} ]
#1.1 Change the value 10 in x to 15
x[1][0] = 15
print(x)

#1.2 Change the last_name of the first student from "Jordan" to "Bryant"
students[0]["last_name"] = "Bryant"
print(students)

#1.3 In the sports_directory, change "Messi" to "Andres"
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

#1.4 Change the value 20 in z to 30
z[0]["y"] = 30
print(z)


#2. Iterate Through a List of Dictionaries
students =[
    {"first_name": "Michael" ,"last_name": "Jordan"},
    {"first_name": "John" ,"last_name": "Rosales"},
    {"first_name": "Mark" ,"last_name": "Guillen"},
    {"first_name": "KB" ,"last_name": "Tonel"}
]
def iterateDictionary(list):
    for i in range(0,len(list)):
        output = ""
        for key,val in list[i].items():
            output += f"{key} - {val}, "
        print(output)
iterateDictionary(students)


#3. Get Values From a List of Dictionaies
def iterateDictionary2(key_name,list):
    for i in range(0,len(list)):
        for key,val in list[i].items():
            if key_name == key:
                print(val)
iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

#4. Iterate Through a Dictionary with List Values
dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank",],
    "instructors": ["Michael", "Amy", "Eduardo", "Josh", "Grahm", "Patrick", "Minh", "Devon", ]
}
def printInfo(dict):
    for key,val in dict.items():
        print(f"{len(val)} {key.upper()}")
        for i in range(0,len(val)):
            print(val[i])

printInfo(dojo)
