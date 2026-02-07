dic={
    1:"khalid",
    2:"robiul",
    3:"farzana",
    4:"kafi",
    5:"jobayer"
}
print(dic[5])
print(dic.items())

dic.update({
    6:"fahad"
})

print(dic.items())

dic2={
    7:"fahim",
    8:"susmi"
}
dic.update(dic2)
print(dic.items())

for key,value in dic.items():
    print(f"Id {key} name is {value}")