
# Secure Web Access using Azure Firewall + Nginx VM

##  Overview

In this project, I designed a secure architecture in Azure where a web server (Nginx) is hosted on a virtual machine without a public IP.

Instead of exposing the VM directly to the internet, all incoming traffic is routed through Azure Firewall using DNAT rules. This ensures controlled and secure access to the application.

---

##  Objective

* Host a static website using Nginx
* Prevent direct internet access to the VM
* Allow access only through Azure Firewall
* Implement NSG rules to restrict traffic

---

##  Architecture

* Virtual Network (VNet)
* Azure Firewall (Public + Private IP)
* Web Subnet
* Linux VM (Private IP only)
* Nginx Web Server

###  Traffic Flow

Internet → Firewall Public IP → DNAT → VM Private IP → Nginx

---

##  Implementation Steps

### 1. Created Virtual Network

* Address space: 10.0.0.0/16
* Subnets:

  * AzureFirewallSubnet (10.0.1.0/26)
  * WebSubnet (10.0.0.0/24)

---

### 2. Deployed Azure Firewall

* Assigned Public IP
* Verified Private IP (10.0.1.4)

---

### 3. Configured DNAT Rule

* Source: My Public IP (for testing)
* Port: 4000
* Destination: Firewall Public IP
* Translated to: 10.0.0.4:80

---

### 4. Created Linux VM

* Ubuntu VM in WebSubnet
* No Public IP assigned
* Installed Nginx:

  ```bash
  sudo apt update
  sudo apt install nginx -y
  ```

---

### 5. Configured NSG Rules

* Applied to WebSubnet

Rules:

* Allow traffic from Firewall Subnet → Port 80
* Deny all other inbound traffic

---

### 6. Testing

* Accessed website via:
  http://<Firewall-Public-IP>:4000
* Verified:

  * Website loads successfully
  * VM is not directly accessible via SSH

---

##  Key Learning

One important observation during this project:

Initially, I allowed traffic only from the firewall private IP (10.0.1.4), but it didn’t work. This is because Azure Firewall performs SNAT, and traffic can originate from multiple internal IPs.

I fixed this by allowing the entire firewall subnet (10.0.1.0/26) in NSG rules.

---

##  Security Highlights

* No public IP on VM
* Controlled access via firewall
* NSG enforcing least privilege
* Reduced attack surface

---

##  Challenges Faced

* NSG rules not working due to incorrect source IP
* Understanding firewall SNAT behavior
* Debugging traffic flow between firewall and VM

---

##  Screenshots

Refer to the screenshots folder for step-by-step visuals.

---

##  Future Improvements

* Add Azure Bastion for secure SSH access
* Implement HTTPS (port 443)
* Integrate Azure Application Gateway (WAF)
* Enable logging and monitoring using Microsoft Sentinel

---

##  Conclusion

This project helped me understand how Azure Firewall and NSG work together to secure applications. It also gave practical exposure to real-world cloud security design patterns.

---
