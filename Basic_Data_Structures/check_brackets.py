# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

#True or False
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
#        print(i,next)
        
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i))

#        print( opening_brackets_stack,len( opening_brackets_stack)  )   
#        print()
        if next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack: # no opening brackets
                return i 
            else:
                top = opening_brackets_stack.pop() #最后一个opening bracket出列 
#                print(top.char, top.position)
                if not are_matching(top.char, next): #配对是否成功
                    return i
           
    if opening_brackets_stack: 
        top = opening_brackets_stack.pop()
        return top.position   

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == None:
        print('Success')
    else:
        print(mismatch+1)
    # Printing answer, write your code here

if __name__ == "__main__":
    main()
