import json
import datetime
try:
    with open("config.json","r") as file:
        config = file.read()
    JsonConfig = json.loads(config)
except Exception:
    print("failed to load the file")
finally:
    pass

dateNow = datetime.datetime.now() 
greeting = "nacht"
if(dateNow.hour > 6):
    greeting = "morgen"
    if(dateNow.hour > 12):
        greeting = "middag"
        if(dateNow.hour > 17):
            greeting = "avond"
            if(dateNow.hour > 20):
                greeting = "nacht"
try:
    print(f"Goede {greeting} {JsonConfig['FirstName']} {JsonConfig['LastName']}")
except Exception:
    try:
        print(F"An error occured by user {JsonConfig['Id']}")
    except Exception:
        print("An error occured with the file")