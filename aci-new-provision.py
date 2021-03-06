# This python script adds a vlan to an existing  pool, and then creates an associated  BD and an EPG
# The program will ask the user for the apic ip address, the apic username and the apic password
# variables that need to be manually changed are : 1) the BD name 2) the vrf name 3) the name of the EPG 4) the vlan number




import requests
from getpass import getpass



requests.packages.urllib3.disable_warnings()

apicip = input("apic ip address")
username = input("apic username: ")
password = getpass('apic password: ')




#generate cookie

#url='https://172.26.1.79/api/aaaLogin.json'
url="https://" + apicip + "/api/aaaLogin.json"




payload = {
  "aaaUser" : {
    "attributes" : {
      "name" : username,
      "pwd" : password
    }
  }
}


response = requests.post(url, json = payload, verify=False)
info=response.json()
token=(info['imdata'][0]['aaaLogin']['attributes']['token'])
print(token)


cookies={
	'APIC-Cookie' : token
	}

# variables

bdname = "bd_core_1.2.3.1_24"
vrf = "vrf_uslab_core"
epg = "epg_mark_test"
vlan = "350"

# add vlan to pool_bd_core

url = "https://" + apicip + "/api/node/mo/uni/infra/vlanns-[pool_bd_core]-static/from-[vlan-" + vlan + "]-to-[vlan-" + vlan + "].json"


payload = {
	"fvnsEncapBlk": {
		"attributes": {
			"dn": "uni/infra/vlanns-[pool_bd_core]-static/from-[vlan-" + vlan + "]-to-[vlan-" + vlan + "]",
			"from": "vlan-" + vlan,
			"to": "vlan-" + vlan,
			"allocMode": "static",
			"rn": "from-[vlan-" + vlan + "]-to-[vlan-" + vlan + "]",
			"status": "created"
		},
		"children": []
	}
}

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json = payload, verify=False, cookies=cookies)

print(response.text.encode('utf8'))
print('Vlan  added to pool - Status Code:' + str(response.status_code))





#create new bd using generated cookie

url = "https://" + apicip + "/api/node/mo/uni/tn-tnt_lab_baremetal_prod/BD-" + bdname + ".json"

payload = {

	"fvBD": {
		"attributes": {
			"OptimizeWanBandwidth": "no",
			"annotation": "",
			"arpFlood": "yes",
			"descr": "",
			"dn": "uni/tn-tnt_lab_baremetal_prod/BD-" + bdname,
			"epClear": "no",
			"epMoveDetectMode": "",
			"hostBasedRouting": "no",
			"intersiteBumTrafficAllow": "no",
			"intersiteL2Stretch": "no",
			"ipLearning": "yes",
			"limitIpLearnToSubnets": "yes",
			"llAddr": "::",
			"mac": "00:22:BD:F8:19:FF",
			"mcastAllow": "no",
			"multiDstPktAct": "bd-flood",
			"name": bdname,
			"nameAlias": "",
			"ownerKey": "",
			"ownerTag": "",
			"type": "regular",
			"unicastRoute": "no",
			"unkMacUcastAct": "proxy",
			"unkMcastAct": "flood",
			"v6unkMcastAct": "flood",
			"vmac": "not-applicable"
		},
		"children": [
			{
				"fvRsMldsn": {
					"attributes": {
						"annotation": "",
						"tnMldSnoopPolName": ""
					}
				}
			},
			{
				"fvRsIgmpsn": {
					"attributes": {
						"annotation": "",
						"tnIgmpSnoopPolName": ""
					}
				}
			},
			{
				"fvRsCtx": {
					"attributes": {
						"annotation": "",
						"tnFvCtxName": vrf
					}
				}
			},
			{
				"fvRsBdToEpRet": {
					"attributes": {
						"annotation": "",
						"resolveAct": "resolve",
						"tnFvEpRetPolName": ""
					}
				}
			},
			{
				"fvRsBDToNdP": {
					"attributes": {
						"annotation": "",
						"tnNdIfPolName": ""
					}
				}
			}
		]
	}
}


headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json = payload, verify=False, cookies=cookies)

print(response.text.encode('utf8'))
print('BD created -  Status Code:' + str(response.status_code))




#epg creation

url = "https://" + apicip + "/api/node/mo/uni/tn-tnt_lab_baremetal_prod/ap-app_profile_baremetal_prod/epg-" + epg + ".json"


payload = {
	"fvAEPg": {
		"attributes": {
			"annotation": "",
			"descr": "",
			"dn": "uni/tn-tnt_lab_baremetal_prod/ap-app_profile_baremetal_prod/epg-" + epg,
			"exceptionTag": "",
			"floodOnEncap": "disabled",
			"fwdCtrl": "",
			"hasMcastSource": "no",
			"isAttrBasedEPg": "no",
			"matchT": "AtleastOne",
			"name": epg,
			"nameAlias": "",
			"pcEnfPref": "unenforced",
			"prefGrMemb": "exclude",
			"prio": "unspecified",
			"shutdown": "no"
		},
		"children": [
			{
				"fvRsPathAtt": {
					"attributes": {
						"annotation": "",
						"descr": "",
						"encap": "vlan-" + vlan,
						"instrImedcy": "immediate",
						"mode": "regular",
						"primaryEncap": "unknown",
						"tDn": "topology/pod-1/protpaths-201-202/pathep-[policy_vpc_201_202_23_24]"
					}
				}
			},
			{
				"fvRsDomAtt": {
					"attributes": {
						"annotation": "",
						"bindingType": "none",
						"classPref": "encap",
						"customEpgName": "",
						"delimiter": "",
						"encap": "unknown",
						"encapMode": "auto",
						"epgCos": "Cos0",
						"epgCosPref": "disabled",
						"instrImedcy": "lazy",
						"lagPolicyName": "",
						"netflowDir": "both",
						"netflowPref": "disabled",
						"numPorts": "0",
						"portAllocation": "none",
						"primaryEncap": "unknown",
						"primaryEncapInner": "unknown",
						"resImedcy": "lazy",
						"secondaryEncapInner": "unknown",
						"switchingMode": "native",
						"tDn": "uni/phys-domain_core",
						"untagged": "no"
					}
				}
			},
			{
				"fvRsCustQosPol": {
					"attributes": {
						"annotation": "",
						"tnQosCustomPolName": ""
					}
				}
			},
			{
				"fvRsBd": {
					"attributes": {
						"annotation": "",
						"tnFvBDName": bdname
					}
				}
			}
		]
	}
}




headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json = payload, verify=False, cookies=cookies)

print(response.text.encode('utf8'))
print('EPG created -  Status Code:' + str(response.status_code))

