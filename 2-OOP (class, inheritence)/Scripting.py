#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Language import Language


class Scripting(Language):
	def getOopSupport(self):
		return self.___oopSupport

	def setOopSupport(self, aOopSupport) -> None:
		self.___oopSupport = aOopSupport

	def getPlatforms(self):
		return self.___platforms

	def setPlatforms(self, aPlatforms) -> None:
		self.___platforms = aPlatforms

	def getAttribute(self):
		pass

	def setAttribute(self, aAttribute) -> None:
		pass

	def __init__(self, name, oopSupport, platforms):
		super().__init__(name)
		self.___oopSupport = oopSupport
		self.___platforms = platforms
		print("\n" +
			  	   name + " is created. It can be used on "
			       + oopSupport+ " operating systems."
			  	   + " Used with these platforms: " + platforms)

