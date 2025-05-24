import json
import random
from config import DATA_PATH

with open(DATA_PATH + "wearable_samples.json") as f:
    wearable_data = json.load(f)

with open(DATA_PATH + "sleep_research.csv") as f:
    research_data = f.readlines()

def get_response(user_query):
    # Simulated intelligent response using wearable + research data
    if "REM" in user_query or "deep sleep" in user_query:
        return "Based on your wearable data, your deep sleep is below optimal levels. Consider avoiding screens 2 hours before bed."
    elif "wake up" in user_query or "routine" in user_query:
        return "Try maintaining a consistent wake-up time. Your current pattern shows irregularity."
    else:
        return random.choice([
            "Ensure a dark room and cool temperature for better sleep.",
            "Consider relaxation techniques before bed to reduce sleep latency."
        ])