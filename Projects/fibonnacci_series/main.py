def fibonnacci_series(n):
    
    a = 0
    b = 1
    if n ==1:
        print(a)
    elif n == 2:
        print (f"{a}\n{b}")
    else:
        print (f"{a}\n{b}")
        for i in range (0, n-2):
            c = a + b  
            a = b
            b = c
            print(c)

n = int(input("Enter a number for fibonacci calculations:"))
fibonnacci_series(n)


"""
Algorithm to be used :
a = 0
b = 1
for loop {
    c = a + b
    a = b
    b = c
}
"""