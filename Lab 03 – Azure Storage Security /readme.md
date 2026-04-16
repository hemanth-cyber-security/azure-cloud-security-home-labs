# Lab 03 – Azure Storage Security (Data Exposure & Secure Access)

## Objective

* Create an Azure Storage Account
* Upload and manage blob data
* Understand risks of public access
* Simulate a real-world misconfiguration
* Implement secure access using RBAC and SAS tokens

---

## Steps Performed

### 1. Created Storage Account

* Created a storage account with standard configuration (LRS, standard tier)

---

### 2. Created Container and Uploaded File

* Created a container named `data-test`
* Uploaded a sample file (`employee-data.txt`)

---

### 3. Verified Default Security

* Container access level was **Private** by default
* File was not accessible publicly

---

### 4. Attempted Public Access (Blocked by Default)

* Tried to enable anonymous access at container level
* Received error indicating public access was disabled at storage account level

---

### 5. Enabled Public Access (For Testing)

* Navigated to:

  * Storage Account → Configuration

* Enabled:

  * **Allow Blob Public Access**

* Changed container access level to:

  * **Blob (anonymous read access)**

---

### 6. Simulated Data Exposure

* Copied blob URL
* Opened in incognito browser

✔ File was accessible without authentication

---

##  Security Risk Identified

* Data exposed to the internet without authentication
* Anyone with the URL could access the file
* Represents a common real-world misconfiguration

---

### 7. Remediation

* Set container access level back to **Private**
* Disabled **Allow Blob Public Access** at storage account level

---

##  Identity-Based Access (RBAC)

* Assigned roles at storage account level:

  * **Reader** (for resource visibility)
  * **Storage Blob Data Reader** (for data access)

* Verified:

  * Authorized user could access data via Azure portal
  * Unauthorized user could not access the data

---

##  Secure Sharing using SAS Token

* Generated SAS token for the blob

* Configured:

  * Read-only access
  * Limited expiry time

* Tested SAS URL:

  * File accessible without login
  * Access limited by token conditions

---

## Key Learnings

* Storage account settings override container-level access
* Public access is a major cause of data breaches
* RBAC provides secure identity-based access
* SAS tokens enable controlled, temporary sharing
* Azure separates management plane and data plane access

---

## Security Best Practices

* Disable public access at storage account level
* Use RBAC for internal access control
* Use SAS tokens for temporary external access
* Follow least privilege principle
* Regularly review storage configurations

---

## Notes

This lab helped me understand how easily data can be exposed due to misconfiguration and how to secure it using identity-based controls and temporary access mechanisms.

---

## Cleanup

* Deleted storage account after testing to avoid charges

---

## Conclusion

This lab demonstrates the complete lifecycle of storage security in Azure, including identifying misconfigurations, exploiting vulnerabilities, and implementing secure access using RBAC and SAS tokens.
