#!/usr/bin/python
from subprocess import Popen
import sys

filename = "Indi.py"
filename2 = "FinalReferendum1.py"
filename3 = "ModiStream.py"
filename4 = "RahulStream.py"
while True:
    print("\nStarting " + filename)
    print("\nStarting " + filename3)
    print("\nStarting " + filename4)
    print("\nStarting " + filename2)
    p = Popen("python " + filename, shell=True)
    p.wait()
    p1 = Popen("python " + filename3, shell=True)
    p1.wait()
    p2 = Popen("python " + filename4, shell=True)
    p2.wait()
    p3 = Popen("python " + filename2, shell=True)
    p3.wait()
