from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

# -----------------------------
# Replace with your values
# -----------------------------
TENANT_ID = "your-tenant-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
KEYVAULT_URL = "https://your-keyvault-name.vault.azure.net/"
SECRET_NAME = "your-secret-name"

# -----------------------------
# Authenticate using App Registration
# -----------------------------
credential = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

# -----------------------------
# Create Secret Client
# -----------------------------
client = SecretClient(
    vault_url=KEYVAULT_URL,
    credential=credential
)

# -----------------------------
# Fetch Secret
# -----------------------------
try:
    secret = client.get_secret(SECRET_NAME)
    print("Secret Value:", secret.value)
except Exception as e:
    print("Error fetching secret:", str(e))