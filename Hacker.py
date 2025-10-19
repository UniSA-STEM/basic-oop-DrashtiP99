"""
File: Hacker.py
Description: This module represents the Hacker character and their actions
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig

class Hacker:
    #initialise the hacker with name, inventory of a single cryptotoken, no rig and a trace level
    def __init__(self, name):
        self._name = name
        self._inventory = []
        self._rig = None
        self._trace_level = 0

        #set the 1 cryptoken in the inventory
        self._inventory.append(Asset("CryptoToken", "Used to acquire or repair rigs"))

    #define the getters for accessing the attributes of the Hackers
    def get_name(self):
        return self._name
    def get_inventory(self):
        return self._inventory
    def get_rig(self):
        return self._rig
    def get_trace_level(self):
        return self._trace_level

    #create method to scan the available inventory and remove asset if found
    def scan_inventory(self, asset_name):
        for asset in self._inventory:
            if asset.get_name() == asset_name:
                self._inventory.remove(asset)
                return asset
        return None

    #method for rig activation which costs 1 token
    def acquire_rig(self, rig=None):
        #need token so scan inventory
        token = self.scan_inventory("CryptoToken")

        if token is None:
            print(f"{self._name} has no CryptoToken to acquire Rig")
            return False
        if rig is None:
            rig = Rig(f"{self._name}'s Rig")
        self._rig = rig
        print(f"{self._name} activated {self._rig.get_name()}")
        return True

    #method to check if rig has been exposed (trace level threshold of 5)
    def check_exposure(self):
        return self._trace_level > 5

    #method for launching data spike by using a Data Spike for rig storage
    #each hit increases opponent rigs damage
    #if opponent rig breaks then hacker can extract unsecured assets by using a removable drive
    #move the extracted assets into own inventory

    def launch_spike(self, target_rig):
        #first check if there is rig in order ot attack
        if self._rig is None:
            print(f"{self._name} require a rig to launch data spike")
            return False
        #check if hacker is exposed
        if self.check_exposure():
            print(f"{self._name} is exposed, can't launch data spike")
            return False
        #otherwise launch the spike consuming the Data spike
        spike = self._rig.release_asset("Data Spike")
        #check if sufficient data spike
        if spike is None:
            print(f"{self._name} has no Data Spikes")
            return False

        #target takes the hit
        target_rig.take_hit()

        #increase the attacking rig's trace level
        self._trace_level += 1

        print(f"{self._name} launched data spike on {target_rig.get_name()}")

        return True

    #the hacker can extract unencrypted assets from the target rif
    #check if broken rig first
    #extraction consumes a removable drive -> check if available or not
    #extraction increases trace level for attacking rig
    def extract_asset(self, target_rig):
        if not self.target_rig.get_broken():
            print(f"Target Rig = {target_rig.get_name()} is not broken. Cannot extract assets")
            return False

        rem_drive = self.scan_inventory("Removable Drive")

        if rem_drive is None:
            print(f"{self._name} does not have Removable Drive for Extraction")
            return False
        self._trace_level += 1

        extracted_assets = []
        for asset in list(target_rig.get_storage()):
            if not asset.encryption_status():
                target_rig.get_storage().remove(asset)
                self._inventory.append(asset)
                extracted_assets.append(asset.get_name())

        if extracted_assets:
            print(f"{self._name} has extracted {', '.join(extracted_assets)}")

        else:
            print(f"No unsecured assets in target = {target_rig.get_name()}")

        return True

    #define methods for asset encryption and decryption
    #consumes a security chip
    #asset can either be in inventory or storage
    def encrypt_asset(self, asset_name, location = "Inventory"):
        security_chip = self.scan_inventory("Security Chip")

        if security_chip is None:
            print(f"{self._name} does not have Security Chip for Encryption")
            return False

        #first find the target asset
        target_asset = None
        if location == "Inventory":
            for asset in self._inventory:
                if asset.get_name() == asset_name:
                    target_asset = asset
                    break
        elif location == "Rig" and self._rig is not None:
            for asset in self._rig.get_storage():
                if asset.get_name() == asset_name:
                    target_asset = asset
                    break
        #check existence and encryption of asset
        if target_asset is None:
            print(f"{asset_name} not found in {location}")
            return False
        if target_asset.encryption_status():
            print(f"{asset_name} is already encrypted")
            return False

        #complete encryption
        target_asset.set_encryption(True)
        print(f"{self._name} has encrypted {asset_name}")
        return True

    #decryption follows same code as above, with set_encryption as False

    def decrypt_asset(self, asset_name, location="Inventory"):

        security_chip = self.scan_inventory("Security Chip")

        if security_chip is None:
            print(f"{self._name} does not have Security Chip for Decryption")
            return False

        # first find the target asset
        target_asset = None
        if location == "Inventory":
            for asset in self._inventory:
                if asset.get_name() == asset_name:
                    target_asset = asset
                    break
        elif location == "Rig" and self._rig is not None:
            for asset in self._rig.get_storage():
                if asset.get_name() == asset_name:
                    target_asset = asset
                    break
        # check existence and decryption of asset
        if target_asset is None:
            print(f"{asset_name} not found in {location}")
            return False
        if not target_asset.encryption_status():
            print(f"{asset_name} is not encrypted")
            return False

        # complete decryption
        target_asset.set_encryption(False)
        print(f"{self._name} has decrypted {asset_name}")
        return True

    #method for upgrading rig which consumes hardware patch
    def upgrade_rig(self):
        hardware_patch = self.scan_inventory("Hardware Patch")

        if self._rig is None:
            print(f"There is no rig to upgrade")
            return False
        if hardware_patch is None:
            print(f"{self._name} does not have a hardware patch for upgrades")
            return False

        #use upgrade() function from Rig class
        self._rig.upgrade(hardware_patch)

        return True

    #method for storing asset's in rig's storage

    def rig_store(self):

















