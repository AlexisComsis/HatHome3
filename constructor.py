import json
import os

class constructor:
    # Create the file config
    def options_txt():
        options = {}
        options["Width"] = 1600
        options["Height"] = 900

        data = json.dumps(options)
        with open("Assets\Data\Options.txt", "w") as file:
            file.write(data)

if not os.path.exists(os.curdir+"Assets\Data"):
    os.mkdir("Assets\Data")
if not os.path.exists(os.curdir+"Assets\Data\Options.txt"):
    constructor.options_txt()
