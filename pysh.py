import os
import subprocess
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style

custom_style = Style.from_dict({
    'pysh': 'ansiblue',
    'folder': 'ansicyan',
    'symbol': 'ansigray',
})
session = PromptSession(
    history=FileHistory('.python_shell_history'),
    auto_suggest=AutoSuggestFromHistory(),
    style=custom_style
)
# I gave this prompt "[Owner@Fedora (current directory)]$", you can change "Fedora" to your current hostname, you can also change "Owner" to your current user, and finally, you can change "$" to "#" if you are in root user.
def get_prompt():
    folder = os.path.basename(os.getcwd()) if os.getcwd() != os.path.expanduser("~") else "~"
    return [
	('class:symbol', '['),
        ('class:pysh', 'Owner@Fedora '),
        ('class:folder', f'{folder}'),
        ('class:symbol', ']'),
	('class:symbol', '$ '),
    ]
def main():
    while True:
        try:
            command = session.prompt(get_prompt())
            
            if not command or not command.strip():
                continue
            
            if command.lower().strip() == "exit":
                break
            
            if command.startswith("py "):
                code = command.split(" ", 1)[1]
                try:
                    exec(code)
                except Exception as e:
                    print(f"Python Error: {e}")
                continue
            
            if command.startswith("cd "):
                parts = command.split(" ", 1)
                target = parts[1] if len(parts) > 1 else os.path.expanduser("~")
                os.chdir(target)
                continue
                
            subprocess.run(command, shell=True)
            
        except (EOFError):
            break
        except (KeyboardInterrupt):
            continue
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    main()
# I am very sorry if this is not good, not perfect, or has many other problems
