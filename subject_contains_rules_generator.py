import json
import os
import copy

if __name__ == "__main__":

    rules_file = "subject_contains_rules.rules"

    if os.path.exists("./"+rules_file) is True:

        print("Using existing "+rules_file+"…")
        f = open("./"+rules_file, "r")
        f_content = json.loads(f.read())
        f.close()
        text = input("Enter the text subject to match for rule: ")
        f_content.append(copy.deepcopy(f_content[0]))
        f_content[-1]["condition"]["subject"]["value"] = (
            ".*" + text + ".*"
        )
        f = open("./"+rules_file, "w")
        f.write(json.dumps(f_content))
        f.close()

    else:
        print("Creating skeleton "+ rules_file  +" file…")

        d = [
            {
                "id": -1,
                "uuid": -1,
                "name": "Subject",
                "order": 10,
                "enabled": True,
                "daily": False,
                "stop": False,
                "condition": {
                    "subject": {
                        "not": False,
                        "value": "",
                        "regex": True,
                    }
                },
                "action": {"type": 15},
                "applied": 0,
            }
        ]

        f = open("./"+rules_file, "w")
        f.write(json.dumps(d))
        f.close()

        f = open("./"+rules_file, "r")
        f_content = json.loads(f.read())
        f.close()
        text = input("Enter the text subject to match for rule: ")
        f_content.append(copy.deepcopy(f_content[0]))
        f_content[-1]["condition"]["subject"]["value"] = (
            ".*" + text + ".*"
        )
        for item in f_content:
            if item.get("id", -1) == -1:
                f_content.remove(item)
        f = open("./"+rules_file, "w")
        f.write(json.dumps(f_content))
        f.close()
