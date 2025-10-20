"""
File: main.py
Description: This module tests the various methods and outputs
Author: Drashti Dineshchandra Patel
ID: 110488649
Username: patdy092
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig
from Hacker import Hacker


#Test Overview
#Test basic setup
#test attack scenario
#test asset extraction
#test encyrption and decryption
#test encryption transfer
#test rig generation
#Test rig upgrades
#test rig repair
#Test storage and retrieval
#all tests

def test_setup():
    #Test the basic setup of hacker and rig
    print("Testing Setup")
    hacker = Hacker("Hashbrown")
    print(hacker)

    hacker.acquire_rig()
    print(hacker)

    print(hacker.get_rig())


def test_attack():
    print("Testing Battle Scenario")
    hack1 = Hacker("Phantom")
    hack1.acquire_rig()
    hack2 = Hacker("Glitch")
    hack2.acquire_rig()

    #set hacker 2 to be the target rig
    target_rig = hack2.get_rig()

    #launching attacks
    print("\nLaunch Data Spikes")
    hack1.launch_spike(target_rig)
    #second spike should break target
    hack1.launch_spike(target_rig)

    print(f"\nHacker 1 = {hack1.get_name()} Launched Attacks -> Trace level = {hack1.get_trace_level()}")
    print(target_rig)
    print()

def test_asset_encryption():
    print("Testing Asset Encryption")
    hacker = Hacker("GhostX")
    hacker.acquire_rig()

    hacker.get_inventory().append(Asset("Security Chip", "Used to encrypt or decrypt assets"))
    hacker.get_inventory().append(Asset("Security Chip", "Used to encrypt or decrypt assets"))
    hacker.get_inventory().append(Asset("Hardware Patch", "Used to upgrade rigs"))

    print(hacker)

    #test encryption with asset = secuirty chip
    print("\nSecurity")
    hacker.encrypt_asset("Security Chip", "Inventory")

    #try to use chip but should fail since encrypted
    print("\nTesting Upgrade with Encrypted Asset")
    fail = hacker.upgrade_rig()

    #should work with decrypted asset
    print("\nDecrypting Asset and Upgrading")
    hacker.decrypt_asset("Security Chip", "Inventory")
    hacker.upgrade_rig()
    print("\nUpgraded Rig:")
    print(hacker.get_rig())
    print()

def test_encryption_transfer():
    print("Testing Encryption Transfer")
    hacker = Hacker("007")
    hacker.acquire_rig()

    hacker.get_rig().store_asset("Security Chip", "Used to encrypt or decrypt assets")
    print(hacker.get_rig())

    print("\nEncrypting data spike")
    hacker.get_inventory().append(Asset("Security", "Used to encrypt or decrypt assets"))
    hacker.encrypt_asset("Data Spike", "Rig")
    hacker.retrieve_from_rig("Data Spike")

    print("\nRetrieving Encrypted Asset and Launching")
    hacker.retrieve_from_rig("Data Spike")

    target_rig = Hacker("Devil")
    target_rig.acquire_rig()
    hacker.launch_spike(target_rig.get_rig())

def test_asset_extraction():
    print("Testing Asset Encryption")
    hack1 = Hacker("Phantom")
    hack1.acquire_rig()
    hack2 = Hacker("Glitch")
    hack2.acquire_rig()

    # set hacker 2 to be the target rig
    target_rig = hack2.get_rig()

    #add to inventory
    hack1.get_inventory().append(Asset("Removable Drive", "Used for Extraction"))
    target_rig = target_rig.get_rig()

    #launch the spike
    hack1.launch_spike(target_rig)
    hack1.launch_spike(target_rig)

    print(f"\nExtracting Assets from Target Rig")
    hack1.extract_asset(target_rig)
    print(hack1)
    print()

#Testing Rig asset creation
def test_rig_creation():
    print("Testing Rig Asset Creation")
    hacker = Hacker("Shield")
    hacker.acquire_rig()
    print(hacker.get_rig())

    print("\n Creating Rig Assets...")
    r = hacker.get_rig()
    r.generate_asset()
    r.generate_asset()
    r.generate_asset()
    r.generate_asset()

    print("\nRig Post-Asset Creation")
    print(r)
    print()


#test rig upgrades using hardware patch asset
def test_rig_upgrade():
    print("Testing Rig Upgrade")
    hacker = Hacker("Shadow")
    hacker.acquire_rig()
    #add 2 hardware patch to hacker's inventory
    hacker.get_inventory().append(Asset("Hardware Patch", "Used to upgrade rigs"))
    hacker.get_inventory().append(Asset("Hardware Patch", "Used to upgrade rigs"))

    print("\nBefore Rig Upgrade:")
    print(hacker.get_rig())

    #then perform two upgrades
    print("\n Upgrading:")
    hacker.upgrade_rig()
    hacker.upgrade_rig()

    print("\n Post Rig Upgrade:")
    print(hacker.get_rig())

    print("\n Test Damage Threshold:")
    r = hacker.get_rig()
    r.take_hit()
    r.take_hit()
    r.take_hit()
    r.take_hit() #take 4 hits to break at level 2

    print(r)
    print()

#test repairing rigs using cryptotoken asset
def test_rig_repair():
    print("Testing Rig Repair")
    hacker = Hacker("Zero")
    hacker.acquire_rig()
    r = hacker.get_rig()
    r.take_hit()
    print(r)

    hacker.get_inventory().append(Asset("CryptoToken", "Used to acquire or repair rigs"))
    token=hacker.scan_inventory("CryptoToken")
    print("\nRepair Rig Post-Damage:")
    r.repair(token)
    print(r)

    #test case for doing a repair when rig is not damaged (should not work)
    print("Testing repair on undamaged rig:")
    hacker.get_inventory().append(Asset("CryptoToken", "Used to acquire or repair rigs"))
    token = hacker.scan_inventory("CryptoToken")
    r.repair(token)
    print(r)
    print()

#test storage of assets
def test_storage():
    print("Testing Storage:")
    hacker = Hacker("007")
    hacker.acquire_rig()
    hacker.get_inventory().append(Asset("Hardware Patch", "Used for Storage"))
    hacker.get_inventory().append(Asset("Removable Drive", "Found in rigs and used for extraction"))
    print("\nOriginal Rig:")
    print(hacker)
    print(hacker.get_rig())

    #store only one asset specifically
    print("\nStore Hardware Patch:")
    hacker.store_to_rig("Hardware Patch")
    print(hacker)
    print(hacker.get_rig()) #check storage of the asset

    print("\nRetrieve Hardware Patch:")
    hacker.retrieve_from_rig("Hardware Patch")
    print(hacker)
    print(hacker.get_rig())
    print()

#tests for edge cases and error handling
def test_edge_cases():
    print("Testing Edge Cases:")

    print("\nTest encryption without available chip:")
    hack1 = Hacker("Echo")
    hack1.acquire_rig()
    hack1.get_inventory().append(Asset("Hardware Patch", "Used to upgrade rigs"))
    hack1.encrypt_asset("Hardware Patch")

    print("\nTest Upgrade without a rig:")
    hack2 = Hacker("Master")
    hack2.get_inventory().append(Asset("Hardware Patch", "Used to upgrade rigs"))
    hack2.upgrade_rig()
    print(hack2.get_rig())

    print("\nTest Extraction from Healthy Rig:")
    hack3 = Hacker("Alpha")
    hack3.acquire_rig()
    hack3.get_inventory().append(Asset("Removable Drive", "Found in rigs and used for extraction"))
    target = Hacker("Beta")
    target.acquire_rig()
    hack3.extract_asset(target.get_rig())

    print("\nTest Attack with High Risk/Trace")
    hack4 = Hacker("Dynamite")
    hack4.acquire_rig()
    #set trace level above 5 (threshold)
    hack4._trace_level = 6

    victim = Hacker("Neon")
    victim.acquire_rig()

    hack4.launch_spike(victim.get_rig())
    print()

#create method to run all tests
def all_tests():
    print("Final Test Suite - Into the Grid:")
    test_setup()
    test_attack()
    test_asset_encryption()
    test_encryption_transfer()
    test_asset_extraction()
    test_rig_creation()
    test_rig_upgrade()
    test_rig_repair()
    test_storage()
    test_edge_cases()
    print("Testing Complete!!")


if __name__ =="__main__":
    all_tests()




















