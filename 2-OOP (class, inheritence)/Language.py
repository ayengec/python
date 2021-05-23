#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Language(object):
	def getName(self):
		print(str(self.___name) + " is created.")
		return self.___name

	def setName(self, aName) -> None:
		self.___name = aName

	def __init__(self, name):
		self.___name = name

