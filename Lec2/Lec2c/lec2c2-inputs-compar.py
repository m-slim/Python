#Learning to take inputs from the user 

#text = input ("Please enter whatever you wish and then you'll be shown the type of data you've input")
#print ("Data you entered is : ' ", text, " 'And is of the type :", type(text))

#As we can see from the above program that whatever the user inputs it 
# becomes a string type ; Therefore if we wish to convert it to other 
# data types then we have to convert it manually 

#----------Method 1-----------------
#text = int (input ("Please enter integer type data"))
#print ("Data you entered is : ' ", text, " 'And is of the type :", type(text))
#---------------------------
 
#Notice that the above expression only takes int as inputs and nothing else

#----------Method 2-------------
#text = input ("Please enter integer type data")
#text = int (text)
#print ("Data you entered is : ' ", text, " 'And is of the type :", type(text))
#-------------------------------


##testing out comparative statements and logical operators on int, float, bool
##string etc
# i>j , i<j, i>=j, i<=j, i == j (True if both equal) , i!=j (True if not equal),
# The above operators can be used to compare ints, floats, ints and floats with eachother
# They can even be used to compare strongs with eachother, which would simply show what alpharbets come before what

#num = 1.3
#num1 = 3

#print (type (num), type (num1))
#ans = num > num1

#print("If num > num1 ", ans)

# Lets try comparing strings with strings


str1 = input ("Enter string one")
str2 = input ("Enter string two")

print (type (str1), type (str2))
ans = str1 > str2

print("If str1 > str2 ", ans)
print("The data type output by these comparative operators is :", type(ans))

# When the string is longer than one charater then it compares onlt the first character of each string

