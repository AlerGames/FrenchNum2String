unaseize = ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix","onze", "douze", "treize", "quatorze", "quinze", "seize"]
dizaines = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante dix", "quatre vingt", "quatre vingt dix"]

#num = input("Input a number between 000 and 999\n")

#you would need to add extra logic so that whenever the user inputs a string it checks that it has 3 digits and that they are all numbers yada yada 

#the arrow is the return type 
def convert(text) -> str:
    output = ""

    #determines the centaine digit
    if(int(text[-3]) == 0):
        output += ""
    elif(int(text[-3]) == 1):   #the if statements are the "exceptions"
        output += "cent "
    else:                       #this else statement is the norm
        output += unaseize[int(text[-3])] + " cent "
    
    #determines the dizaine and unite digit
    if(70 < int(text[1:]) < 77 or 90 < int(text[1:]) < 97):     #check if between 70 and 76 for the exceptions
        output += dizaines[int(text[1]) - 1] + " " + unaseize[int(text[2]) + 10]
    elif(10 < int(text[1:]) < 17):
        output += unaseize[int(text[1:])]
    else:
        output += dizaines[int(text[1])] + " " + unaseize[int(text[2])]    

    return output
        
#print(convert(num))
times = 0
while(times < 1000):
    if(times < 10):
        print(convert("00" + str(times)) + "\n")
    elif(10 <= times < 100):
        print(convert("0" + str(times)) + "\n")
    else:
        print(convert(str(times)) + "\n")
    times += 1
