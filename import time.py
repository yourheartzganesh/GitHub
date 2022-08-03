# import time 

# # def c_to_f(c):
    
# #     return (c*9/5)+32 
    
# # start_time = time.perf_counter()
# # print(start_time)
# # c_to_f(100000)
# # end_time = time.perf_counter()
# # print(end_time)
# # print('calculation speed: ',end_time-start_time)

# def check_if_a_element_in_a_list(list,ele):
    
#     for i in list:
        
#         if i == ele:
            
#             return True
         
#     return  False

# st = time.perf_counter()
# list = [1,3,4,5,6,7,8,90,1,2,3,2,2]

# ele = int(input("Enter the number: "))

# print(check_if_a_element_in_a_list(list,ele))

# et = time.perf_counter()

# print(et-st)

def find_fact(n):
    
    answer = 1 
    
    while(n>1):
        
        answer *= n 
        n -= 1 
    
    return answer

print(find_fact(900000))