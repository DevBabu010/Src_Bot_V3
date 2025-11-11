# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "24665004")
API_HASH = os.getenv("API_HASH", "95a3af611f8956b0ed9c238c3bb7835b")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8250086707:AAEWRn9vXJ5giw5VuqN8c-Zr9gzUU91DL-c")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://manishmern:mernlearning@mycluster.d0eojtt.mongodb.net")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5740631254").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "tg_downloader")
STRING = os.getenv("STRING", "BQF4W6wAC2rqtshJSBIJ5Amae9VE7P3uvqX2gUqvaHiOcZrJ45p9Igl16wHUcnIdecSKzcEwYROGXGwnU3iwqJg9B2zJZbkEhtoRW4_MZfTfrcCh1PByvpFexc5qKsEkJRHoStlATXyNZPgL2EQGaCvUt67nYU6x37zScklERoQBp6PwNdaxQxV72FCbC7vQnI_frJjNWD4CCrGkvHDLBPl0o9R2NTLnbyvO6lXwyJaN181NdDhDUoHoda6JtmxrOQUp-zUHHIvaATcPmqLU1cMjmVWVRCk_PqPn-IeWCFRFiR8Yg5T_VCL-Y4vnGliM7eTSOdtU7w7ALQTjc53T9HCguK4FPwAAAAFWKxTWAA") # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1003026701939")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002449510249")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3YhY7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx6XpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "00"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/bot_subscription") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/Rahul_p4")

