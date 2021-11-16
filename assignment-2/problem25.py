def digit_number(number):
    
    x=str(number)
    if "." in x:
        dot=x.index(".")
        c=x[:dot]
        d=len(c)
        print(dot)
    sum_even=0
    sum_odd=0
    sum_0=0
    
    number=float(number)
    digit=number
    for x in range(0,d):
        number%=10
        if number==0:
            sum_0+=1
        elif number%2!=0:
            sum_odd+=1
        else:
            sum_even+=1
        digit//=10
        number=digit
    t=("sum of 0=",sum_0,"sum of even numbers=",sum_even,"sum of odd numbers=",sum_odd)
    return (t)
number=float(input("enter float number:"))
print(digit_number(number))