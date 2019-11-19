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

