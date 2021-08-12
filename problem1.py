for t in range (int(input())):      #Read number of test cases to be run
    s = list(input().strip())       # create list s  and dividing string into unique set of characters from the input 
    r = sorted(s)                   # create sorted list r for sorting the characters of string
    x = set(r)                      #converting sorted list into set for not doing any modifications
    a = []                          # create empty list a for storing the numbers to be added
    flag = 0                      
    count = 0                       # define int variable to indicate position if a number 
    for n in x:                     # read each element in set x and append it to a by counting the element.
        a.append(r.count(n))
    val = sorted(a)                 #sort a list and store it in val
    for k in range(2, len(val)):    #read each element k from 2 to length of val
        if val[k] == val[k-1]+val[k-2]:         #check ehether the number is the sum of it's two previous number 
            fib = True              # if satisfies store it as True in fib
            if fib:                 # if fib satisfies, increment the flag
                flag = 1
        else:                       #else store it as False in fib
            fib = False
    if fib or flag or len(x)<3:     #if it is equal to fib or flag length of x is less than 3, then print Dynamic
        print("Dynamic")
    else:                           #else print Not
        print("Not")