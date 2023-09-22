import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
ACTOR_ID = os.getenv("ACTOR_ID")
URL_TO_PARSE = os.getenv("URL_TO_PARSE", default="https://www.csi-dmc.com")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", default="csi-dmc_scrapy_output.json")
