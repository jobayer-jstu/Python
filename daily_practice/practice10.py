animals=["cow","cat","dog","tiger","fox"]
print(animals)

animals.append("lion")
print(animals)

animals.extend(["goat","sheep","ash"])
print(animals)

ani= animals.pop(8)
print(animals)

num=[23,4,44,65,232,55,677]
num.sort()
print(num)

num.reverse()
print(num)

num=num[::-1]
numb= num[3:7]
print(numb)

numb= num[:-2]
print(numb)

numb=num[::-1]
print(numb)

new=animals+num
print(new)