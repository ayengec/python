#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Language import Language

class HardwareDesign(Language):
	def getPldType(self):
		return self.___pldType

	def setPldType(self, aPldType) -> None:
		self.___pldType = aPldType

	def getPinNumber(self):
		return self.___pinNumber

	def setPinNumber(self, aPinNumber) -> None:
		self.___pinNumber = aPinNumber

	def calculatePower(self, aUsedLutNum, aUsedRamNum):
		return aUsedRamNum*0.017 + aUsedLutNum*0.008

	def __init__(self, name):
		super().__init__(name)

