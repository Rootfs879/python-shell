import os
import subprocess
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style

custom_style = Style.from_dict({
    'pyzsh': 'ansiblue',
    'folder': 'ansicyan',
    'symbol': 'ansigray',
})

from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.shell import BashLexer

session = PromptSession(
    history=FileHistory('.python_shell_history'),
    auto_suggest=AutoSuggestFromHistory(),
    style=custom_style
)

def get_prompt():
    folder = os.path.basename(os.getcwd()) if os.getcwd() != os.path.expanduser("~") else "~"
    return [
	('class:symbol', '['),
        ('class:pyzsh', 'Owner@Fedora '),
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
