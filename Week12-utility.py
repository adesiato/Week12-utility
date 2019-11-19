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


def FindWordCount(list1, string1):
    new_list1 = []
    new_string1 = ""

    for val in list1:
        new_list1.append(val.lower())

    new_string1 = string1.lower()

    count = 0
    for val in new_list1:
        if new_string1 in val:
            count += 1
    print("OUTPUT %d" % (count))
    

def ScoreFinder(list1, list2, string):
    new_list1 = []
    new_string = ""
    
    for name in list1:
        new_list1.append(name.lower())
        
    new_string = string.lower()

    if new_string in new_list1:
        score_index = new_list1.index(new_string)
        score = str(list2[score_index])
        print("OUTPUT %s got a score of %s" % (list1[score_index], score))
    else:
        print("OUTPUT player not found")


def Union(list1, list2):
    combined = list1 + list2
    new_list = []
    count = 1

    for val in combined:
        if val in new_list:
            continue
        else:
            new_list.append(val)
    
    print(new_list)
