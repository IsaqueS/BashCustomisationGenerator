# Bash customization generator

This is meant for personal use, so its very simple.

1. Create bash.toml file
2. Create an script.sh file to add your own script
3. Execute

### Example of the 'bash.toml' file:
```path="~/.bash_aliases" # Export Path

[alias]
please="sudo" # Very easy to understand

[uv-local-to-global]
ytmanager=["~/Documentos/Code/Projetos/Python/YTManager","ytmanager"] # Makes an uv env script global (1: Path, 2: "script/Command to execute")
genbash=["~/Documentos/Apps/BashCustomisationGenerator/","generate_bash_settings.py"]```