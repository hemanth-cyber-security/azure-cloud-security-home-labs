# Lab 02 – Identity and Access Management in Azure

## Objective

* Create and manage users in Microsoft Entra ID
* Assign roles using RBAC
* Validate access based on least privilege
* Configure MFA and Conditional Access
* Understand real-world MFA behavior and troubleshooting

---

## Steps Performed

### 1. Created Users

* Created test users:

  * `user1-sec`
  * `user2-sec`
  * `user3-test` (used for clean validation)

---

### 2. Assigned Roles (RBAC)

Roles were assigned at the Resource Group level:

* user1-sec → **Reader**
* user2-sec → **Contributor**

---

### 3. Access Validation

* Logged in as **user1-sec**

  * Able to view resources
  * Unable to create or modify resources

* Logged in as **user2-sec**

  * Able to create and modify resources

---

### 4. MFA Configuration

* Enabled and tested per-user MFA
* Later disabled per-user MFA to test behavior

---

### 5. Conditional Access (CA)

* Created a Conditional Access policy to require MFA
* Initially configured in **Report-only mode** for testing

---

### 6. MFA Behavior Testing and Troubleshooting

Observed unexpected MFA prompts even when:

* Security Defaults → Disabled
* Per-user MFA → Disabled
* Conditional Access → Report-only

---

## Investigation

* Checked **Sign-in Logs**
* Observed:

  * Authentication requirement → *Single-factor authentication*

This confirmed that MFA was **not enforced by policy**

---

## Root Cause

* The MFA prompts were due to:

  * Authentication method registration
  * Session/token validation after registration

* Not due to Conditional Access or per-user MFA

---

## Key Observations

* Conditional Access in report-only mode does not enforce MFA
* Sign-in logs are the most reliable source to confirm authentication behavior
* MFA prompts can occur even without enforcement due to registration or session behavior

---

## Security Practices Applied

* Principle of Least Privilege using RBAC
* Role assignment at appropriate scope (Resource Group level)
* Identity-based access validation
* Troubleshooting authentication behavior using logs

---

## Notes

This lab helped me understand that identity is the primary security control in Azure.
It also highlighted how MFA behavior can sometimes be confusing and why log analysis is important to determine the actual enforcement.

---

## Cleanup

* Deleted Resource Group after testing
* Retained users for further identity-related labs

---

## Conclusion

This lab demonstrates how to manage access using RBAC and how to implement and troubleshoot MFA and Conditional Access in Azure.
It also reflects real-world scenarios where authentication behavior needs to be analyzed using logs rather than relying only on user prompts.
