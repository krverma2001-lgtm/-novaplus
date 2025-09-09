#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22471119"))
API_HASH = environ.get("API_HASH", "b8ab98fab8020ad7eab4c38f1ec9e1ae")
BOT_TOKEN = environ.get("BOT_TOKEN", "8340702693:AAH4qk8TR0xBParuTIqlcCKTChZPW8RkGVE")

OWNER = int(environ.get("OWNER", "5504044604"))
CREDIT = environ.get("CREDIT", "NOVAPULSE𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1371497919').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1371497919').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set



