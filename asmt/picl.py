from pickling import *


def func():
     l=[ ]
     f=open("kkkk.dat","ab")
     rn = int(input("Enter Room Number : "))
     pr = int(input("Enter the price of room: "))
     rt = input("Enter the type of room: ")
     L  = [rn, pr, rt]
     dump(L, f)
     print("Record added in the file")
     f.close()
func()
