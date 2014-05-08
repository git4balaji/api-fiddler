#! /usr/bin/env python3
import yaml
import json
from randomgen import RandomGen

class TypeError(RuntimeError):
    pass

class ObjectParser:
    """ A object parser"""
    
    def __init__(self, data):
        self.objects = {}
        for key,value in data.items():
            self.objects[key] = Object(value)
    
    def __str__(self):
        return "objectParser:\n{0}".format( "\n%%\n".join([name + ":" + str(object) for name,object in self.objects.items() ] ) )
    
    def getData(self, request):
        object = {};
        if request in self.objects:
            return json.dumps(self.objects[request].json())
        else:
            raise IOError
            

class Object:
    """ This is a  """
    def __init__(self, data):
        self.items = {}
        self.generator = RandomGen()
        for key,value in data.items():
            self.items[key] = value
    
    def __str__(self):
        return "Items:\n{0}".format( "\n%%\n".join([name + ":" + object for name,object in self.items.items() ] ) )
    
    def gen(self, datatype):
        if hasattr(self.generator, datatype):
            return getattr(self.generator, datatype)()
        else:
            raise TypeError
    
    def json(self):
        return {name: self.gen(datatype) for name,datatype in self.items.items()}
