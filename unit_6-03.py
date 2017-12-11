# Created by: James Lee
# Created on: Dec 2017
# Created for: ICS3U
# This program displays an example of a structure

class Address():
    # this class is the structure for the canada post address
    def __init__(self, name, street_number, street_name, street_type, city, province, postal_code):
        self.name = name
        self.street_number = street_number
        self.street_name = street_name
        self.street_type = street_type
        self.city = city
        self.province = province
        self.postal_code = postal_code


user_name = raw_input("Enter your name: ")
user_street_number = raw_input("Enter your street number: ")
user_street_name = raw_input("Enter your street name: ")
user_street_type = raw_input("Enter your street type: ")
user_city = raw_input("Enter your city: ")
user_province_or_territory = raw_input("Enter your province or territory: ")
user_postal_code = raw_input("Enter your postal code: ")

user_input = Address(user_name, user_street_number, user_street_name, user_street_type, user_city, user_province_or_territory, user_postal_code)

print(user_input.name + '\n' + user_input.street_number + ' ' + user_input.street_name + ' ' + user_input.street_type + '\n' + user_input.city + ' ' + user_input.province + ' ' + user_input.postal_code)
