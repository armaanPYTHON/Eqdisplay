import os




def read_list(file, separator):
    if os.path.isfile(file):

        mylist = []

        f = open(file, 'r', encoding='utf8')
        for line in f.readlines():
            line = line.strip(separator)
            mylist.append(line)
        f.close()
        return mylist
    else: return 'This file path does not exist'






def delete_object(file, separator, object):

    if os.path.isfile(file):

        mylist = []

        f = open(file, 'r')
        for line in f.readlines():
            line = line.strip(separator)
            mylist.append(line)
        f.close()
        
        if object in mylist:
            mylist.remove(object)
        else:
            return 'Error! The given object is not present in the given file, hence it cannot be delete'
        
        f = open(file, 'w')
        for line in mylist:
            f.write(line+separator)
        f.close()

        return 'Object deleted'
    
    else: return 'This file path does not exist'






def add_object(file, separator, object):
    if os.path.isfile(file):
        mylist = []

        f = open(file, 'r', encoding="utf8")
        for line in f.readlines():
            line = line.strip(separator)
            mylist.append(line)
        f.close()
        
        mylist.append(object)
        
        f = open(file, 'w', encoding="utf8")
        for line in mylist:
            f.write(line+separator)
        f.close()

        return 'Object Added'

    else: return 'This file path does not exist'
    
def write(file, object):
    if os.path.isfile(file):
        
        f = open(file, 'wb')
        f.write(object)
        f.close()

        return 'Object Added'

    else: return 'This file path does not exist'
    
    
def read_encoded(file):
    if os.path.isfile(file):
        f = open(file, 'r', encoding='utf8')
        string = f.read()
        f.close()

        return string

    else: return 'This file path does not exist'




def read_string(file):
    if os.path.isfile(file):
        f = open(file, 'r', encoding="utf8")
        string = f.read()
        f.close()

        return string

    else: return 'This file path does not exist'





def add_list(file, separator, list):

    if os.path.isfile(file):

        mylist = []

        

        f = open(file, 'r')
        for line in f.readlines():
            line = line.strip(separator)
            mylist.append(line)
        f.close()

        for item in list:
            mylist.append(item)

        
        f = open(file, 'w')
        for line in mylist:
            f.write(line+separator)
        f.close()

        return 'All objects in list Added'

    else: return 'This file path does not exist'






def delete_list(file, separator, list):

    if os.path.isfile(file):
    
        mylist = []

        f = open(file, 'r')
        for line in f.readlines():
            line = line.strip(separator)
            mylist.append(line)
        f.close()
        
        for item in list:
            if item in mylist:
                mylist.remove(item)
            else:
                return 'Error! The given object is not present in the given file, hence it cannot be delete'
        
        f = open(file, 'w')
        for line in mylist:
            f.write(line+separator)
        f.close()

        return 'All Objects in list deleted'
    
    else: return 'This file path does not exist'