#Name :Ethan Mbila
#Date :12/02/2026
#String formatting

sentence = "I watch anime too"
string_length = len(sentence)

print(f"The length is: {string_length}")

#splitting a string
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

#print(f"The first subject is:", split[0])

#make everything caps
code = "ub132hfuflyhe"
caps = code.upper()

#print("New MPesa code", caps)

uncaps = caps.lower()

print("New MPesa code", uncaps)

#Replacing characters in a string
bal = "Ksh210"
added = "Ksh253"
clean_bal = bal.replace("Ksh", "")

print("Cleaned balance:", clean_bal)

clean_added = added.replace("Ksh", "")

print("Cleaned amount added:", clean_added)

cleaner_bal = int(clean_bal)
cleaner_added = int(clean_added)
sum = cleaner_bal + cleaner_added

print("Your new balance is", sum)

#challenge
bal2 = "Ksh120"
message = "CONFIRMED: you have received Ksh40 from Phillip"
munyun = message.split(" ")
clean_bal2 = bal2.replace("Ksh"," ")
clean_munyun = munyun[4].replace("Ksh"," ")
new_bal = int(clean_bal2) + int(clean_munyun)

print("yo new balance is", new_bal)