"""
File: main.py
Description: This module tests the various methods and outputs
Author: Drashti Dinechandra Patel
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

def encryption_transfer():
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






