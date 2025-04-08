import json
import os


class suppliers:
    def __init__(self,password, name, phone, person, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.id = 0
        self.password = password
        self.name = name
        self.phone = phone
        self.person = person

    def __repr__(self):
        return f"Supplier(id={self.id}, name='{self.name}', phone='{self.phone}', person='{self.person}')"
    
    def to_dict(self):
        return {
            "password": self.password,
            "name": self.name,
            "phone": self.phone,
            "person": self.person,
            "items": self.items,
            "id": self.id
        }
    