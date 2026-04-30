#  Azure Key Vault – Secret Retrieval using Entra ID App (Hands-on Lab)

##  What I did in this lab

In this lab, I wanted to understand how applications securely fetch secrets from Azure instead of hardcoding them.

So I built a simple setup where:

* I stored a secret in Azure Key Vault
* I created an application in Entra ID
* Gave that app permission to read the secret
* Wrote a Python script to fetch the secret

This helped me understand how authentication and secret management actually works in real-world cloud environments.

---

##  My Understanding of the Flow

Here’s how I understood the process step by step:

1. I registered an application in Microsoft Entra ID
   → This acts as the identity of my application

2. I created a **client secret** for that app
   → This is like a password for the application

3. Then I created a secret inside Azure Key Vault

4. I gave my application **Get Secret permission only** using access policy
   → Following least privilege

5. When my Python script runs:

   * It sends Client ID + Client Secret to Entra ID
   * Entra ID verifies and gives an **access token**
   * That token is then used to call Key Vault
   * Key Vault checks permissions and returns the secret

 So basically:

> The app first proves its identity, gets a token, and then uses that token to securely access the secret.

---

## ⚙️ Setup I Performed

### 1. Created Key Vault

* Added a secret (example: `db-password`)

### 2. Registered Application

* Got Client ID and Tenant ID

### 3. Created Client Secret

* Saved it securely (cannot be retrieved again)

### 4. Configured Access Policy

* Selected my app
* Gave only **Get** permission

---

##  Python Script Explanation

I used Python with Azure SDK.

### Authentication part

```python
credential = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)
```

Here:

* My app is authenticating with Entra ID
* Internally, it gets an access token

---

### Connecting to Key Vault

```python
client = SecretClient(
    vault_url=KEYVAULT_URL,
    credential=credential
)
```

This sets up the connection to Key Vault using that token.

---

### Fetching the secret

```python
secret = client.get_secret(SECRET_NAME)
print(secret.value)
```

This is where:

* The request goes to Key Vault
* Token is validated
* Permission is checked
* Secret is returned

---

##  Security Learnings

While doing this lab, I understood a few important things:

* Client secret is very sensitive → should never be exposed
* Always follow **least privilege** (only Get permission)
* If client secret is leaked, attacker can access secrets
* Managed Identity is a better option in real environments

---

##  From a SOC / Security Perspective

Thinking from a SOC analyst point of view:

* We should monitor Key Vault access logs
* Look for unusual secret access patterns
* Detect if an application suddenly starts pulling many secrets
* Track authentication logs from Entra ID

---

##  Screenshots Included

I’ve added screenshots for:

* App registration
* Client secret creation
* Key Vault secret
* Access policy configuration
* Python output

---

##  What I plan to do next

* Try the same using **Managed Identity**
* Create a detection scenario in Azure Sentinel
* Simulate secret access abuse and monitor logs

---

##  Final Thoughts

This lab helped me connect multiple concepts:

* Identity (Entra ID)
* Secret management (Key Vault)
* Authentication (OAuth token flow)

It’s a simple setup, but very important for real-world cloud security.

---
