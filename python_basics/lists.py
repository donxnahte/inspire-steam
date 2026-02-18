#Name :Ethan Mbila
#Date :18/02/2026
#lists

list1 = ["loaf", "bread", "container", "milk", "Joe", "Dirt", "DVD"]
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
list1.append("slowed")
print(list1)

list2 = ["konami", "kojima", "bethesda", "tencent"]
print(len(list2))

list3 = list1 + list2
print(list3)

list2.pop()
print(list3)

list3.insert(0, "a")
list3.insert(9, "Vallary")
print(list3)

list3.extend("SOARIN")
print(list3)

list3.remove("Vallary")
print(list3)

list4 = list3.copy()
print(list4)