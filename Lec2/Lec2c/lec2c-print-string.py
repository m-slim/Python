print ("Hello i'm the code in lecture 2 - python <3")
print ("We're going to learn about strings today")

name = "Muhammad"
greeting = "Asalamoalaikum" 

sentence = greeting + " " + name

print ("So my new sentence is :", sentence) 
print ("So my new sentence is :", sentence)

#if i use a multiplier wuth a string ; python interprets it as repeat 
# (- and / dont mean anything)
#that string that number of times
#In python parenthesis () indicate to python what to solve first so

sentence = greeting + (" " + name)*2

print("So NOW my sentence is :", sentence)

#we can also assign a number and turn it into a string ; Lets see what it does

num = 1
print("The num is of type :", type(num))

strnum = str(num)

print("Now the number has been turned", strnum)

print("The num NOW is of type :", type(strnum))

#This has to be done because we can not add a number to a string 
#All data types have to be of the same type when they are computed

print("Look at this example ", num, " ", strnum, "Is this valid?")

#using commas add spaces and using + doesn't add any commas

print ("Lets look at this"+strnum)

print ("Lets look at this"+strnum) #Turn this to num for experiment

# The above line becomes invalid unless its changed to a string data type
