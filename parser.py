#! /usr/bin/end python3

from object
import yaml

data = yaml.load( open('outline.yaml', 'r') )
myobject = object(data)
print(myobject)


class objectParser:
    """ A object parser"""

    def __init__(self,data)
		self.objects = {}
		for key,value in data.items():
			self.objects[key] = Object(objects[key])

    def __str__(self)
		return "objectParser:\n{0}".format( "\n%%\n".join([name + ":" + str(object) for name,object in self.objects.items() ] ) ) 


class Object:
	""" This is a  """
	
	def __init__(self,data):
		self.items = []
		for item in data:
			self.item.append(item)


	
