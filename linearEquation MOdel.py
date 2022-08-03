import time
def find_the_linear_timing(List):
    
    adding_list = []
    for ele in List:
        
        start_time = time.time()
        
        add = ele + 1  
        
        adding_list.append(add)
        
        print(time.time() - start_time)
   
 
chenck = find_the_linear_timing([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])