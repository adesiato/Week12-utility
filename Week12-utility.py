# Anthony Desiato
# CSCI 102 - Section A
# Week 12 - Lab A

def PrintOutput(string):
    print("OUTPUT %s" % (string))

def LoadFile(filename):
    bruh = open(filename, "r")
    contents = bruh.read()
    new = contents.split("\n")
    print("OUTPUT %s" % (new))

def UpdateString(string1, string2, index_int):
    list_1 = []
    for val in string1:
        list_1.append(val)
    list_1[index_int] = string2
    new_string = ""
    print("OUTPUT %s" % (new_string.join(list_1)))



