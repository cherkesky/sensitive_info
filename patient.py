'''
Practice: Sensitive Information
Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

Social security number
Date of birth
Health insurance account number
First name
Last name
Address
The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter.
'''

class Patient:
  def __init__ (self, social_security_number, date_of_birth, insurance, first_name, last_name, address):
    self.__social_security_number = social_security_number
    self.__date_of_birth = date_of_birth
    self.__insurance = insurance
    self.__first_name = first_name
    self.__last_name = last_name
    self.__address = address

  @property
  def social_security_number(self):
    try:
      return self.__social_security_number[7:]
    except AttributeError:
      return 0
  @property
  def date_of_birth(self):
    try:
      return self.date_of_birth[5:]
    except AttributeError:
      return 0
      
  # @property
  # def first_name(self):
  #   try:
  #     return self.__first_name+ " " + self.__last_name
  #   except AttributeError:
  #     return 0
  # @property
  # def last_name(self):
  #   try:
  #     return self.__first_name+ " " + self.__last_name
  #   except AttributeError:
  #     return 0
  @property
  def full_name(self):
    try:
      return self.__first_name+ " " + self.__last_name
    except AttributeError:
      return 0

  @property
  def address(self):
    try:
      return self.__address
    except AttributeError:
      return 0
      
  @address.setter
  def address(self, address):
    self.__address = address


cashew = Patient("097-23-1003", "08/13/92", "7001294103", "Daniela", "Agnoletti", "500 Infinity Way")

# This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# Neither should this
# cashew.date_of_birth = "01-30-90"

# # But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# # These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)
# # But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"

cashew.address = "123 Rainbow St"

print(cashew.address)