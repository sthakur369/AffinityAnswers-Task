# Imports
import requests
import json
import pandas as pd
import re

# Extract PINCODE mentioned in the address
def pinextract(address):
  pattern = r'\b[0-9]{6}\b' #it means it will only look for a 6-digit number
  pin = re.findall(pattern, address)
  
  if len(pin) > 0:
    return pin[0]
  else:  #if PIN is missing or doesn't have 6-digit length
    print('PIN should always be 6-digit no. Given PIN is Invalid or PIN is not present in address')
    print()
    print('INCORRECT Address')
    return None

# We had extracted pin from address, now we will fetch all the info of that pincode using API call
def pin_check(pincode):
  api_url = f"https://api.postalpincode.in/pincode/{pincode}"
  response = requests.get(api_url)

  if response.status_code == 200:
    data = response.json()

    # If given pincode looks fine by length but have no data linked to that pincode then 'Status' will be 'Error'
    if data[0]['Status'] != 'Success':
      print(f"For given Pincode {pincode}: {data[0]['Message']}")
      print('INCORRECT Address')
      return None
    else:
      return data


  else:
    print(response.status_code, response.reason)
    return None

# We had extracted pincode and then fetched data related to that pincode, Now we will check our given addr. is part of the pincode or not
def address_check(data, address):
  flag = False
  state_flag = False

  # lowering the case is just for standarization
  for i in range(0, len(data)):
    if data[i]['Name'].lower() in address.lower():
      flag = True
  
  # If address is correct but it has missing State Name(just for an extra check!)
  for i in range(0, len(data)):
    if data[i]['State'].lower() in address.lower():
      state_flag = True



  if flag == True:
    if state_flag == False:
      print('{WARNING}:: You have not mentioned STATE NAME in your address!')

    return 'Correct Address'
  else:
    return 'INCORRECT Address'


# taking the input
address = str(input('Enter the Address:  '))

# calling the functions
data = None
pincode = None
# if address is not given
if len(address) > 0:
  pincode = pinextract(address)
else:
  print('No Address is given')

if pincode:
  data = pin_check(pincode)
if data:
  data = data[0]['PostOffice']
  print(address_check(data, address))
