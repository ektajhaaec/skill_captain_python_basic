def reverseVowel(str):
    #print(str[0])
    vowels = ['a','e','i','o','u']
    #list = [x for x in str if x in vowels ]
    #print(list)
    # mujhe start wale 1st wala  vowel firnd ker k  last element se compare kerna h. jab vowel milega to interchange ker dena h . 
    #
    str = list(str)
    # a= len(str)
    # for i in range (len(str)) :
        
    #         if str[i]  in vowels:
                
    #             for j in range(a-1,1,-1) :
                    
    #                     if str[j] in vowels :
    #                         n =str[i] 
    #                         str[i]  =  str[j]
    #                         str[j] = n
    #                         a=j 
                        
    #                         break

    left = 0
    right = len(str)-1
    while left<right:
        if str[left] in vowels and str[right] in vowels :
            n =str[left] 
            str[left]  =  str[right]
            str[right] = n
            right -=1
            left +=1
        elif str[left] in vowels and str[right] not in vowels :
            right -=1
        elif str[left] in vowels and str[right] in vowels :
            left +=1
        else:
            right -=1
            left +=1
    return str

user_input = input("Enter a string\n")
print(reverseVowel(user_input))

