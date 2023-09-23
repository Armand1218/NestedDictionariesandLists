#1) Udpates Values in dict and lists.
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])

z[0]["y"] = 30
print(z)

#2) Iterate through a list of dictionary
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#3)get values from a list opf dictionaries
def iterate_dict(list):
    for i in range(0, len(list) - 1):
        result = ""
        for key,val in list[i].items():
            result += f"{key} - {val},"
        print(result)
iterate_dict(students)

def iterate_students(key_name, list):
    for i in range(0, len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_students("first_name", students)
iterate_students("last_name", students)

#4)iterate through a dictionary with lists values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key,val in dict.items():
        print("------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])
printInfo(dojo)
