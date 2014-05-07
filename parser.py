#! /usr/bin/env python3
import yaml

class ObjectParser:
    """ A object parser"""
    
    def __init__(self, data):
        self.objects = {}
        for key,value in data.items():
            self.objects[key] = Object(value)
    
    def __str__(self):
        return "objectParser:\n{0}".format( "\n%%\n".join([name + ":" + str(object) for name,object in self.objects.items() ] ) )

class Object:
    """ This is a  """
    def __init__(self, data):
        self.items = {}
        for key,value in data.items():
            self.items[key] = value
    
    def __str__(self):
        return "Items:\n{0}".format( "\n%%\n".join([name + ":" + object for name,object in self.items.items() ] ) )

data = yaml.load( open('outline.yaml', 'r') )
myobject = ObjectParser(data)
print(myobject)