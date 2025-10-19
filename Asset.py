"""
File: Asset.py
Description: This module represents the asset items in the Cyberpunk Simulation
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset():
    #initialise the asset
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._encryption = False #set false since assets are not encrypted by default

    #need to define methods to access the names, descriptions and check encryptions
    def get_name(self):
        return self._name
    def get_description(self):
        return self._description
    def encryption_status(self):
        return self._encryption

    #need to set the encryption status of asset
    def set_encryption(self, encryption):
        self._encryption = encryption

    #string conversion method to format asset
    def __str__(self):
        if self._encryption:
            return f"{self._name}: {self._description}[Encrypted]"
        else:
            return f"{self._name}: {self._description}"



