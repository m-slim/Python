# if <condition>:
#     <expression>
#     <expression>

text = int(input("Enter text"))
num = int (input ("Enter num"))

#if num>=text:
#    out=text + num
#    print ("num is greater than text and result is ", out)

#else:
#    print ("num is less than text")

# Lets try nested if statements

if num>=text:
    print ("num is greater than or equal to text")
    if num>text:
        out = num - text
        print ("Num is greater than text therefore the difference is", out)
    else:
        out = num - text
        print ("Both numbers are equal so the difference is", out)

else:
    out = text - num
    print ("num is less than text so the difference between text and num is", out)
