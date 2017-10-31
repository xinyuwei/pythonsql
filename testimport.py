import globaldata

print(globaldata.GlobalData.a)

globaldata.GlobalData.a = 80

print(globaldata.GlobalData.a)

y = globaldata.GlobalData.a

print(y)

from globaldata import b

print(b)

print(globaldata.b)

globaldata.b = 500

print(b)

print(globaldata.b)