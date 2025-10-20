"""
File: Rig.py
Description: Represents the Hacker's computer system and main tool for hacking
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
import random

class Rig:
    #initialise the rig
    def __init__(self, name):
        self._name = name
        self._damage_count = 0
        self._broken_state = False
        self._storage = []
        self._upgrade_lvl = 0
        self._max_storage = 5 #base capacity of the storage

    #Append starting assets - 2 Data Spikes and 1 removable drive
    #Note Asset form = (name, description)
        self._storage.append(Asset("Data Spike", "Used in battles"))
        self._storage.append(Asset("Data Spike", "Used in battles"))
        self._storage.append(Asset("Removable Drive", " Found in rigs and used for extraction"))


    #define the getters for the accessing the attributes
    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage_count

    def get_broken(self):
        return self._broken_state

    def get_storage(self):
        return self._storage

    def get_upgrade_lvl(self):
        return self._upgrade_lvl


    #define methods for performing the actions/mechanics of the rig

    #check if damaged rig or broken and repair using a crypotoken, return Bool based on repair state
    def repair(self, crypto_token):
        if self._damage_count > 0 or self._broken_state:
            #reset damage count and broken state
            self._damage_count = 0
            self._broken_state = False
            print(f"{self._name} has been repaired")
            return True
        else:
            print(f"{self._name} does not require repair")
            return False

    #perform upgrades using hardware patch and increment level
    def upgrade(self, hardware_patch):
        self._upgrade_lvl += 1
        self._max_storage +=3
        print(f"{self._name} has been upgraded to level = {self._upgrade_lvl}\n Storage Capacity = {self._max_storage}")

    #Rigs can take a hit from data spikes which increases damage level by 1
    def take_hit(self):
        self._damage_count += 1
        #set the damage threshold (if exceeded, then rig is broken)
        damage_limit = 2 + self._upgrade_lvl

        if self._damage_count >= damage_limit:
            self._broken_state = True
            print(f"{self._name} is broken")
        else:
            print(f"{self._name} has taken a hit (Damage level = {self._damage_count})")

    #Rig can generate random assets
    def generate_asset(self):
        #define all asset types possible
        asset_list = [("Data Spike", "Used in battles"),
                      ("CryptoToken", "Used to acquire or repair rigs"),
                      ("Removable Drive", "Found in rigs and used for extraction"),
                      ("Security Chip", "Used to encrypt or decrypt assets"),
                      ("Hardware Patch", "Used to upgrade rigs")]
        #randomly select from the possible assets
        asset_selection = random.choice(asset_list)
        #create the asset object for this new asset and then add to the storage
        new_asset = Asset(asset_selection[0], asset_selection[1])
        self._storage.append(new_asset)
        print(f"{self._name} Generated Asset = {new_asset.get_name()}")
        return new_asset

    #Rigs can store and release assets, which allows transfer to and from the storage
    #note that encrypted assets are protected and cannot be moved until decrypted

    #store the given asset into the storage list
    def store_asset(self, asset):
        if len(self._storage) >= self._max_storage:
            print(f"{self._nqme} the storage is full!")
            return False
        self._storage.append(asset)
        return True

    #release given asset from storage list if not encrypted
    def release_asset(self, name_asset):
        for a in self._storage:
            if a.get_name() == name_asset:
                if a.encryption_status():
                    print(f"{name_asset} is encrypted so it can't be released")
                    return None
                self._storage.remove(a)
                return a
        return None

    #return the condition/state of the rig based on damage, broken and upgrade levels
    def get_rig_state(self):
        if self._damage_count == 0:
            return f"Pristine (Level {self._upgrade_lvl})"
        elif self._broken_state:
            return f"Broken (Level {self._upgrade_lvl})"
        else:
            return f"Damaged (Level {self._damage_count})"

    #get the string representation of the rig including the name, condition/state, storage list
    def __str__(self):
        store_list = ",".join([asset.get_name() for asset in self._storage])

        return f"Rig Name:{self._name}, Condition: {self.get_rig_state()}, Storage:[{store_list}] ({len(self._storage)}/{self._max_storage})"

























