#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Language import Language


class SoftwareDesign(Language):
	def getLangTree(self):
		return self.___langTree

	def setLangTree(self, aLangTree) -> None:
		self.___langTree = aLangTree

	def getOpSystem(self):
		return self.___opSystem

	def setOpSystem(self, aOpSystem) -> None:
		self.___opSystem = aOpSystem

	def getSize(self):
		return self.___size

	def setSize(self, aSize) -> None:
		self.___size = aSize

	def showAllFeatures(self):
		pass

	def evaluatePerf(self, aThreadUsage, aJdkDepend, aCoreNum):
		pass

	def __init__(self, name):
		super().__init__(name)


