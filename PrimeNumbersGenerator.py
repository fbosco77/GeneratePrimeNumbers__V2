'''
Created on Jun 13, 2022

@author: fbosco

V2
'''

import sys
import PrimeNumber


def IsMainEntryPoint():
    return __name__ == "__main__"


if IsMainEntryPoint():
    
    if (len(sys.argv) >= 2):
        if len(sys.argv) > 2:
            print("More than one argument provided. Will only consider the 1st one")
        
            
        try:
            inputNumber = int(sys.argv[1])
        except:
            print(f"Argument \"{sys.argv[1]}\" is not an integer")
            sys.exit(0)
            
            
        if inputNumber < 2:
            print(f"\"{inputNumber}\" is not a valid input. Must be an integer greater than \"1\".") 
            sys.exit(0)   
        
        
        try:
            output = PrimeNumber.PrimeNumberCalculator.GetAllPrimesUpToNumber(inputNumber)
        
            print(output)
        except Exception as e:
            print(e)
            
            
    else:
        print("Please provide as argument an integer value greater than or equal to \"2\"")
        
