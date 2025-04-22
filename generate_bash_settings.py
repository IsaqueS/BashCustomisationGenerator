import os
from pathlib import Path
import tomllib
import sys
from typing import Any

BASH_INFO_PATH = "bash.toml"

BASH_SCRIPT_PATH = "script.sh"

BASH_FILE_PATH = Path(os.path.expanduser("~")) / "Documentos"

BASH_EXPORT_PATH: str = "~/.bash_aliases"

def main():
    if not os.path.exists(BASH_INFO_PATH):
        print(f"'{BASH_INFO_PATH}' file not found!")
        sys.exit(1)
    
    file = open(BASH_INFO_PATH, "rb")

    data: dict[str, Any] = tomllib.load(file)

    global BASH_EXPORT_PATH
    
    if data.get("path", None):
        BASH_EXPORT_PATH = data["path"]
    else:
        print(f"Using default export path: {os.path.expanduser(BASH_EXPORT_PATH)}\n\nTo define an path add an path value on bash.toml file, like this: 'path='[path here!]'")

    aliases: list[str] = ["#!/bin/bash", "# Script to generate bash file by IsaqueS", "# repo: https://github.com/IsaqueS/BashCustomisationGenerator", "# Aliases starts here:"]

    aliases_text = []

    for alias in data.get("alias", {}).keys():
        aliases_text.append(
            f"alias {alias}=\"{data["alias"][alias]}\""
        )
    
    aliases.append("\n".join(aliases_text))

    del aliases_text
    
    aliases.append("# python/uv global remaps starts here:")
    
    for python_script in data.get("uv-local-to-global", {}).keys():
        alias: list[str] = data["uv-local-to-global"][python_script]

        if not isinstance(alias,list) and alias.size() >= 2:
            print("The value must be an list! (1. path, 2. script/command). from key: %s"%python_script)
            sys.exit(1)

        if not os.path.exists(os.path.expanduser(alias[0])):
            print("The first value of the list must be an valid path! from key: %s"%python_script)
            sys.exit(1)

        aliases.append("%s () {    \n(cd \"%s\" && uv run \"%s\" \"$@\")\n}"%(
            python_script,
            os.path.expanduser(alias[0]),
            alias[1]
            ),
        )
    
    aliases.append("# 'script.sh' contents starts here:")
        
    if os.path.exists(BASH_SCRIPT_PATH):
        with open(BASH_SCRIPT_PATH, "rt") as file:
            file_text: str = file.read()
            file_text = file_text.replace("#!/bin/bash", "")
            aliases.append(file_text)

    with open(os.path.expanduser(BASH_EXPORT_PATH), "wt") as file:
        file.write("\n\n".join(aliases))
    
    print("File generated!")

if __name__ == "__main__":
    main()