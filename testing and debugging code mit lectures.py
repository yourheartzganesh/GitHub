from pickletools import string1
import unittest 

def summation(a):
    total = 0 
    for i in a:
        total += i 
    
    return total 

def multiplication(a):
    total_mul = 1
    for i in a:
        total_mul *= i 
    
    return total_mul

def rightPosition(string1,string2):
    """
    return the count of right positioned letters

    Args:
        string1 (Stirng): letters of char
        string2 (String): letters of char
    """
    
    right_position = 0 
    
    for i in range(len(string1)):
        
        if(string1[i]==string2[i]):
            
            right_position += 1 
    
    return right_position

def common_letters(string1,string2):
    
    string1dict = {}
    print(string1dict)
    string2dict = {}
    print(string2dict)
    commonL = 0 
    
    for char in string1:
        
        if(char in string1dict):
            string1dict[char] += 1 
        else:
            string1dict[char] = 1
    
    for char in string2:
        
        if(char in string2dict):
            
            string2dict[char] += 1 
        else:
            
            string2dict[char] = 1 
    
    
    for letter in string1:
        if(string2dict.get(letter) != None and string2dict[letter]>0):
            if(letter in string2dict):
                commonL += 1 
                string2dict[letter] -= 1 
    return commonL
        
class SummMult(unittest.TestCase):
    
    def test_summation(self):
        check1 = summation([1,2,3,4,5])
        self.assertEqual(check1,15)
    
    def test_multiplication(self):
        a = [1,2,3,0]
        check2 = multiplication(a)
        self.assertEqual(check2,0)
        
    def test_common_letters(self):
        
        string1 = "AABC"
        string2 = "AAFR"
        check3 = common_letters(string1,string2)
        self.assertEqual(check3,2)
    
    def test_rightPosition(self):
        string1 = "AABC"
        string2 = "AAFR"
        check4 = rightPosition(string1,string2)
        self.assertEqual(check4,2)
        
if __name__ == '__main__':
    
    unittest.main()
    
    # y = common_letters(string1="maths",string2="sciee")
    # print(y)
    # x = rightPosition(string1="hsenid",string2="dinesh")
    # print(x)
    # a = [1,2,3,4]
    # assert summation(a) == 10,"Should be 10"
    # assert multiplication(a) == 24,"Should be 24"
    # print("Everything is passed")