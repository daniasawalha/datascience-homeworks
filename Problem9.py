def Count(sentence):
    sum_of_vowel=0
    sum_of_consonants=0
    a=sentence.count('a')
    u=sentence.count('u')
    i=sentence.count('i')
    e=sentence.count('e')
    o=sentence.count('o')
    sum_of_vowel=a+u+i+o+e
    
    for x in sentence:
        if (x.isalpha() and x !="o" and x!="u" and x!="i" and x!="a" and x!="e" and x!=" "):
            sum_of_consonants +=1
    print("vowels=",sum_of_vowel,"consonants=",sum_of_consonants)
    
sentence=(str(input("input an English sentence=")))
Count(sentence.lower()
      )




p=(input("enter to continue......"))

