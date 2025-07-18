import json
import os
import copy

if __name__ == "__main__":
    if os.path.exists("./ip_rules.rules") is True:
        print("Using existing ip_rules.rules…")
        f = open("./ip_rules.rules", "r")
        f_content = json.loads(f.read())
        f.close()
        new_ip = input("Enter the IP address to add to the file: ")
        f_content.append(copy.deepcopy(f_content[0]))
        f_content[-1]["condition"]["header"]["value"] = (
            ".*sender IP is " + new_ip + ".*"
        )
        f = open("./ip_rules.rules", "w")
        f.write(json.dumps(f_content))
        f.close()

    else:
        print("Creating skeleton ip_rules.rules file…")

        d = [
            {
                "id": -1,
                "uuid": -1,
                "name": "IP",
                "order": 10,
                "enabled": True,
                "daily": False,
                "stop": False,
                "condition": {
                    "header": {
                        "not": False,
                        "value": ".*sender IP is 0.0.0.0.*",
                        "regex": True,
                    }
                },
                "action": {"type": 15},
                "applied": 0,
            }
        ]

        f = open("./ip_rules.rules", "w")
        f.write(json.dumps(d))
        f.close()

        f = open("./ip_rules.rules", "r")
        f_content = json.loads(f.read())
        f.close()
        new_ip = input("Enter the IP address to add to the file: ")
        f_content.append(copy.deepcopy(f_content[0]))
        f_content[-1]["condition"]["header"]["value"] = (
            ".*sender IP is " + new_ip + ".*"
        )
        f = open("./ip_rules.rules", "w")
        f.write(json.dumps(f_content))
        f.close()
