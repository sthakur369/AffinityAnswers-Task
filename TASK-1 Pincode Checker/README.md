# Pincode Checker
This code will take address as input and check whether the given address is correct or not w.r.t PINCODE.

**Run command:**
``` python Pincode_Checker.py ``` 



## Test Case 1 - [Correct address]
> 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050

> 2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050

**O/P:** Correct Address


## Test Case 2 - [Incorrect address]

> 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095

> Colony, Bengaluru, Karnataka 560050

**O/P:** INCORRECT Address


## Test Case 3 - [Missing Pincode in Address]

> 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka

**O/P:** 
PIN should always be 6-digit no. Given PIN is Invalid or PIN is not present in address

INCORRECT Address




## Test Case 4 - [Invalid Pincode Number in Address]

> 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka, 12345678912354654686546654165

**O/P:**
PIN should always be 6-digit no. Given PIN is Invalid or PIN is not present in address

INCORRECT Address




## Test Case 5 - [Blank Pincodes in Address]

> 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka, 176120

**O/P:**
For given Pincode 176120: No data found

INCORRECT Address




## Test Case 6 - [Correct address having missing state name]:: *[WARNING Test Case]*

> 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, 560050

**O/P:**
{WARNING}:: You have not mentioned STATE NAME in your address!

Correct Address






