'''
Created on Jun 14, 2022

@author: fbosco

V2
'''

import unittest
import PrimeNumber


class Test(unittest.TestCase):


    def testFirstPrime(self):
        self.assertEqual([2], PrimeNumber.PrimeNumberCalculator.GetAllPrimesUpToNumber(2))

    def testFirstTwoPrimes(self):
        self.assertEqual([2,3], PrimeNumber.PrimeNumberCalculator.GetAllPrimesUpToNumber(3))
        
    def testFirstComposite(self):
        self.assertEqual([2,3], PrimeNumber.PrimeNumberCalculator.GetAllPrimesUpToNumber(4))

    def testFirstPrimeAfterFirstComposite(self):
        self.assertEqual([2,3,5], PrimeNumber.PrimeNumberCalculator.GetAllPrimesUpToNumber(5))
               
    def testPrimeListFor__70(self):
        self.assertEqual([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67], PrimeNumber.PrimeNumberCalculator.GetAllPrimesUpToNumber(70))  
        
    def test100ThPrime(self):
        primes = PrimeNumber.PrimeNumberCalculator.GetAllPrimesUpToNumber(546)
        self.assertEqual(primes[99], 541)              



if __name__ == "__main__":
    unittest.main()