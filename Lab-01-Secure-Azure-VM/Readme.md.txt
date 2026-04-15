#lab01 secure azure vm

objective

create vm
configure nsg,vnet
restrict ssh from unkown ip -accept only from my ip

----------

steps performed

created a Resource group - named -RG-securitylab
created vNet - vnet-lab
subnet

deployed vm of linux based -attached nsg and vnet 

NSG  -in nsg configured inbound rule to ssh from my public ip
     denied all other inbound traffic.



verified the ssh access from my ip - success
tried to login from other network -denied .



security practice

network level -- leasr priviledge 
restricted inbound traffic from other network 
avoided exposing the vm to public internet




