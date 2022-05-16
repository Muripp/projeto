equação = input("")
contador = 0
for i in range(len(equação)):
    print(equação[i])
    if equação[i] == "(" or equação[i] ==  "[" or equação[i] ==  "{":
        print("add")
        contador += 1
    if equação[i] == ")" or equação[i] == "[" or equação[i] == "{":
        print("remove")
        contador -= 1
if contador == 0:
    print("ta certa!")
else:
    print("tA ERRADA!")

