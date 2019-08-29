def string_rev1(string):
    words = string.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords) 
    return newSentence 

def string_rev2(string):
    inputword = string.split(" ")
    inputword = inputword[-1::-1]
    output = ' '.join(inputword) 
    return output 



string=input("ENTER THE STRING")
reversestring1=string_rev1(string)
print(reversestring1)
reversestring2=string_rev2(string)
print(reversestring2)
