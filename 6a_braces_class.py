class braces:
    def __init__ (self):
        self.string = None

    def setter(self):
        self.string =input('ENTER THE STRING: ')

    def check(self):
        open_braces = ["[","{","("]
        close_braces = ["]","}",")"]
        stack = []
        for i in string: 
            if i in open_braces: 
                stack.append(i)
            elif i in close_braces: 
                pos = close_braces.index(i) 
                if ((len(stack) > 0) and
                    (open_braces[pos] == stack[len(stack)-1])): 
                    stack.pop() 
                else: 
                    return "Unbalanced"
        if len(stack) == 0: 
            return "Balanced"
    
        
b = braces()
string = input('ENTER A STRING')
print(string,"-", b.check()) 

''' *******************************OUTPUT*****************************

TC1: 
ENTER A STRING{[(){}]}
{[(){}]} - Balanced

TC2:
ENTER A STRING{}{{[}}]()
{}{{[}}]() - Unbalanced


