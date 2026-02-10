import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return{
                "theme" : "light",
                "language": "en",
                "notifications": True
                }
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)
        
        
def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)
        
def update_setting(key,value):
    config =load_config()
    config[key]=value
    save_config(config)
    
print("current config:", load_config())
update_setting("theme", "dark")
print ("updated config:", load_config())



print(type(load_config()["notifications"]))
