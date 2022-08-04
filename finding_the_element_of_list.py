def finding_the_element_of_a_list(list,element):
    
    x = 200 
    print(x)
    length_of_list_index = len(list)-1 
    
    if(length_of_list_index % 2 == 0 ):
        
        middle_element_index = length_of_list_index//2 
    
    else:
        
        middle_element_index = (length_of_list_index+1)//2 
        
    if(element == list[middle_element_index]):
        
        return list[middle_element_index]
    
    if(len(list) == 1):
        
        return None 
    
    if(element < list[middle_element_index]):
        
        new_list = list[:middle_element_index]
        
    else:
        
        new_list = list[middle_element_index+1:]
        
    recursive_call = finding_the_element_of_a_list(new_list,element)
    
    return recursive_call

def intToStr(i):
    
    digits = '0123456789'
    
    result = ""
    
    if i == 0 :
        
        return "0"
    
    while i > 0 :
        
        result = digits[i%10]+result
        
        i = i//10 
        
    return result

def finding_the_subset(s):
    
    length_set = len(s)
    
    return 2**length_set


print(finding_the_subset({1,2,3,4}))


# print(intToStr(32))

# L = [1,2,3,4,5,6,7,8,9]

# user_input = int(input("Enter the number you want to check with in list:  "))

# check_input_in_list = finding_the_element_of_a_list(L,user_input)

# if(user_input == check_input_in_list):
    
#     print("Yeah your input in this list! Congrats!!!!")

# else:
    
#     print("Oops!! Sorry your input is not list...")