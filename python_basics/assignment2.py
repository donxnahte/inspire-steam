#Ethan Mbila
#12/02/2026
#string formatting
bal2 = "Ksh120"
message = "CONFIRMED: you have received Ksh40 from Phillip"
munyun = message.split(" ")
clean_bal2 = bal2.replace("Ksh"," ")
clean_munyun = munyun[4].replace("Ksh"," ")
new_bal = int(clean_bal2) + int(clean_munyun)

print("yo new balance is", new_bal)