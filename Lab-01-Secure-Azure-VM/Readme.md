# Lab 01 – Secure Azure VM

## Objective

* Create a virtual machine in Azure
* Configure a Network Security Group (NSG)
* Restrict SSH access so that only my IP can connect

---

## Steps Performed

* Created a Resource Group named **RG-securitylab**

* Created a Virtual Network (**vnet-lab**) with a subnet

* Deployed a Linux virtual machine and attached it to the VNet and NSG

* Configured NSG inbound rule:

  * Allowed SSH (port 22) only from my public IP
  * Denied all other inbound traffic

---

## Validation

* Verified SSH access from my IP → **Success**
* Attempted access from a different network → **Blocked**

---

## Security Practices Applied

* Applied **least privilege at the network level**
* Restricted inbound access to a trusted IP only
* Reduced exposure of the VM to the public internet

---

## Notes

This lab helped me understand how easily a VM can be exposed if NSG rules are not configured properly, and why restricting access is critical in cloud environments.
