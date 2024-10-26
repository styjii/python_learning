import os
import json

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(CURR_DIR, "setting.json")

with open(FILE, "r") as f :
    setting = json.load(f)

    
setting["fontSize"] = 15

with open(FILE, "w") as f:
    json.dump(setting, f, indent=4)