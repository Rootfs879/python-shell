# Pysh

A lightweight command-line shell built with Python. Designed specifically for Linux/Unix-based systems (including Termux on Android).

## Features
- [x] Executes system commands (e.g., `ls`, `cd`, `grep`, etc.).
- [x] Supports directory navigation (`cd`).
- [x] Includes command history functionality.
- [x] Lightweight and optimized for low memory usage.
- [x] Clean error handling (graceful exit on Ctrl+C and Ctrl+D).
- [x] Has REPL feature (use `repl` in py-shell+repl.py, not pysh.py).
## How to Use

1. **Ensure Python is installed** on your system.

2. **Download the file**

3. Run the Shell/REPL.

   a. If you choose Shell file, do
      ```bash
         python pysh.py
      ```

   b. If you choose REPL file, do
      ```bash
         python py-repl.py
      ```

   c. If you choose Shell+REPL file, do
      ```bash
         python py-shell+repl.py
      ```
4. (Optional) You can use REPL in the Shell+REPL file, how to do it? You can use `repl` to switch to REPL mode.

5. Important!!! You need to install two package, namely `pygments` and `prompt_toolkit`.

The method:
```bash
   pip install pygments prompt_toolkit
```

## Requirements
* ~~Python 3.x~~
* Python 3.8.x

## Contributing

This project is open-source. If you would like to add features or fix bugs, feel free to submit a Pull Request.

## License

This project is licensed under the **MIT License**.

## Reminder

Once again, **a version for Windows is not yet available** or still under construction.

## Additional

You can read [CONTRIBUTING.md](https://github.com/Rootfs879/python-shell/blob/main/CONTRIBUTING.md) or [LICENSE](https://github.com/Rootfs879/python-shell/blob/main/LICENSE) if you want.


PS: If you found this repo from a tutorial or a blog, please let me know by opening an issue!
