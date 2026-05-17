# FPick

[![Release](https://github.com/coding-beagle/fpick/actions/workflows/release.yml/badge.svg)](https://github.com/coding-beagle/fpick/actions/workflows/release.yml)

FPick is a simple utility that allows users to access their OS file dialog from the CLI.

This is particularly useful for image / video browsing with scripts.

## Download and Installation

Download the latest release for your system [here](https://github.com/coding-beagle/fpick/releases).

Pick the binary that matches your OS:

- **Windows** — `fpick-windows.exe`
- **macOS** — `fpick-macos`
- **Linux** — `fpick-linux`

### Windows

1. Download `fpick-windows.exe` from the [releases page](https://github.com/coding-beagle/fpick/releases).
2. Rename it to `fpick.exe`.
3. Move it to a folder on your `PATH` ([tutorial here](https://windowsloop.com/how-to-add-to-windows-path/)) - for example, create `C:\Tools\` and add it to your PATH via *System Properties → Environment Variables*.
4. Open a new terminal and run `fpick` to confirm it works.

> **Note:** Windows SmartScreen may warn that the publisher is unverified the first time you run it, since the binary isn't code-signed. Click *More info → Run anyway*. If your antivirus flags it, this is a [common false positive with PyInstaller binaries](https://github.com/pyinstaller/pyinstaller/issues/5854).

### macOS

1. Download `fpick-macos` from the [releases page](https://github.com/coding-beagle/fpick/releases).
2. Open Terminal and make it executable:
```bash
   chmod +x ~/Downloads/fpick-macos
```
3. Move it onto your `PATH`:
```bash
   sudo mv ~/Downloads/fpick-macos /usr/local/bin/fpick
```
4. Run `fpick` to confirm it works.

> **Note:** Because the binary isn't notarized with Apple, Gatekeeper will block it on first launch. To allow it, either:
> - Right-click the file in Finder → *Open* → *Open* (one-time bypass), or
> - Run `xattr -d com.apple.quarantine /usr/local/bin/fpick` after moving it.

### Linux

1. Download `fpick-linux` from the [releases page](https://github.com/coding-beagle/fpick/releases).
2. Make it executable and move it onto your `PATH`:
```bash
   chmod +x ~/Downloads/fpick-linux
   sudo mv ~/Downloads/fpick-linux /usr/local/bin/fpick
```
3. Run `fpick` to confirm it works.

> **Note:** `fpick` uses Tkinter for its file dialog, which depends on Tcl/Tk system libraries. On most desktop distros these are already present. If you get a `Tcl/Tk` error, install them:
> - Debian/Ubuntu: `sudo apt install tk`
> - Fedora: `sudo dnf install tk`
> - Arch: `sudo pacman -S tk`

### Install via pip (any OS)

If you have Python 3.10+ installed, you can skip the binary entirely:

```bash
pipx install fpick
```

This is the recommended option for developers — `pipx` handles isolation automatically and updates with `pipx upgrade fpick`. If you don't have `pipx`, install it with `pip install --user pipx`.

## Example usage

Running a python script that takes an image or video file as an output:

```
python some_script.py `fpick`
```

For those unfamiliar with terminal use (I.E. the primary target for this tool): 

```
# either way works
echo `fpick`  # the backticks are command substitution: the output of 'fpick' is passed as the argument to 'echo'
echo $(fpick) # more modern syntax for command substitution
```

![](./readme_resources/first_demo.gif)

Use the '-d' or '--directory' flags to return directories only:

![](./readme_resources/directory_demo.gif)

Use the '-f' or '--file_extension' flags to filter by file extension:

![](./readme_resources/filefilter_demo.gif)

## To create a release build:

```
git tag v0.1.0 && git push origin v0.1.0
```

Any tag starting with v and numerical version number should work (?)
