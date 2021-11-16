def permute(l1,start,end,seperator=' '):
    count =0
    y=len(l1)
    out=""
    for x in range(start,end-1):
        x=2
        q=(y-x)*(y-1)*y
        
        w=q//2
        l=[]
    for i in range(w):
        
            l1[1],l1[-1] = l1[-1],l1[1]
            string =""
            out += string.join(l1) + ", "
            l1[0],l1[1]=l1[1],l1[0]
            string =""
            out += string.join(l1) + ", "
    out = "{" + out[0:-2] + "}"
    print(out)
   
            
        
word=(list(input("enter at least 3 charecters:")))
e=len(word)
permute(word,0,e-1,',')
