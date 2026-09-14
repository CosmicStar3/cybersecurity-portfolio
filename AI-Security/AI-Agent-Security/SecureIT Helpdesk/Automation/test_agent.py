import os
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv("COPILOT_CONNECTION_STRING")

if not connection_string:
    raise ValueError("COPILOT_CONNECTION_STRING not found in .env")

print("Connection string loaded successfully.")
print("Automation environment is ready.")