a = (input(":"))
b = str(input(":"))
list = [a,b]
my_dict = {
    "Anna" :1969 ,
    "name" : "Nick",
    "City" : "lviv"
}


for x in my_dict.values():
    if x in list:
        print("yes")
    else:
        print("no")
