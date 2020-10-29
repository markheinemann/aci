# aci
marks aci related python scripts

<b>1) aci-new-provision.py <br /><br /></b>

-This python script adds a  new vlan to an existing vlan pool under Fabric/Access Policies, and then it will create a new associated  BD and  EPG  for that vlan <br /><br />
-The program will initially ask the user for the apic ip address, the apic username and the apic password <br /><br />
-A session cookie will then be generated <br /><br />
-variables that need to be manually changed in the script  by the user are : <br /><br />
a) the BD name  <br />
b) the vrf name  <br />
c) the name of the EPG  <br />
d) the vlan number <br />
