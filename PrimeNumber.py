'''
Created on Jun 13, 2022

@author: fbosco

V2
'''

from math import sqrt


class PrimeNumberCalculator(object):
    '''
    Statement: A prime number is a number greater than 1 with only two factors, themselves and 1.
    In other words, a prime number cannot be divided by any other numbers without leaving a remainder.
    '''
    
    
    @staticmethod
    def __IsPrime(number):
        if number > 1:
            #Simple "Trial Division": check if evenly divisible by any number between 2 and number^1/2:
            for n in range(2, int(sqrt(number)) + 1):
                if (number % n) == 0:
                    return False
            
            return True
        
        else:
            return False       
    
    
    @staticmethod
    def __SieveOfEratosthenes(stopNumber):
        mapping = [True] * (stopNumber + 1) #create initial list of booleans with all numbers up to "stopNumber"
         
        #First 2 entries correspond to numbers 0 and 1, which are NOT prime.
        #So we can already flag them to "False":
        mapping[0] = False
        mapping[1] = False   
         
        i = 2
        while(i * i <= stopNumber): #Essentially, if "stopNumber" is 2 or 3, won't go into loop and 2 and 3 remain flagged
            if(mapping[i]): #if number has not been "tagged" yet, it could be a prime number
                j = i * i  #numbers of the form "integer^2" are not prime...
                
                while(j <= stopNumber):
                    mapping[j] = False  
                    j += i  #...and neither the following +i, +2i, +3i, etc....
                    
            i += 1
            
        return mapping    
    
    
    @staticmethod
    def GetAllPrimesUpToNumber(stopNumber):
        if type(stopNumber) == int and stopNumber > 1:
            
            mapping = PrimeNumberCalculator.__SieveOfEratosthenes(stopNumber)
            
            primeList = [];
            
            for n in range(len(mapping)):
                if(mapping[n]):
                    primeList.append(n)
                    
            return primeList
            
        else:
            raise Exception(f"\"{stopNumber}\" is not a valid input. Must be an integer greater than 1.")
        
    
                