# aci
marks aci related python scripts

1) aci-new-provision.py <br />

-This python script adds a  new vlan to an existing pool, and then creates an associated  BD and an EPG for that vlan <br />
-The program will ask the user for the apic ip address, the apic username and the apic password <br />
-A session cookie will then be generated <br />
-variables that need to be manually changed in the script  are : <br />
a) the BD name  <br />
b) the vrf name  <br />
c) the name of the EPG  <br />
d) the vlan number <br />
