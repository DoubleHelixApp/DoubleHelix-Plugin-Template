import os
import shlex
import subprocess
import sys

if __name__ == "__main__":
    commands = [
        "git init",
        "git add .",
        "git commit -m \"First commit\"",
        "git remote add origin {{cookiecutter.repository}}",
        "git branch -M main",
    ]
    print(os.getcwd())
    for command in commands:
        subprocess.check_call(shlex.split(command))