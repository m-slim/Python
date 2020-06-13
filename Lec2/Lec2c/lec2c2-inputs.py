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
text = input ("Please enter integer type data")
text = int (text)
print ("Data you entered is : ' ", text, " 'And is of the type :", type(text))
#-------------------------------


