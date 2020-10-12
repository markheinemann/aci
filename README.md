# aci
marks aci related python scripts

1) aci-new-provision.py

# -This python script adds a  new vlan to an existing pool, and then creates an associated  BD and an EPG for that vlan
# -The program will ask the user for the apic ip address, the apic username and the apic password
# -A session cookie will then be generated
# -variables that need to be manually changed in the script  are :
a) the BD name 
b) the vrf name 
c) the name of the EPG 
d) the vlan number
