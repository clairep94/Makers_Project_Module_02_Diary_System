from typing import Any
from lib.Contact import Contact

class ContactList():
    def __init__(self) -> None:
        self.all_contacts = []
    
    def add(self, contact: Contact):
        self.all_contacts.append(contact)
    
    def extract_nums_from(text:str):
        #create a list of all substrings in text that satisfy:
            #len = 11
            #char in string in "1234567890"
        #for num in list:
            #self.add(num)
    
    def delete(self, contact: Contact):
        self.all_contacts.remove(contact)

    def update_name(self, contact: Contact, name:str):
        