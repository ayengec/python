from HardwareDesign import HardwareDesign
from Scripting import Scripting
from SoftwareDesign import SoftwareDesign

myFpga = HardwareDesign("Artix-7")
myFpga.getName()                    # come from Language Base Class!
print(format(myFpga.calculatePower(48, 196)) + " Watt")

myPython = Scripting("Pyhton3", "Windows/Linux/MacOS", "PC/MCU")

myJava = SoftwareDesign("java8")
myJava.getName()
myJava.setLangTree("JDK")
print(myJava.getLangTree())
