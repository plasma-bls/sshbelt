# ssh-belt

ssh-belt is a lightweight Python script that scans a system for installed SSH clients, terminal emulators, and remote access tools by checking common installation paths.

It supports Linux and Windows, including Flatpak applications on Linux, and prints the results in a clean, colorized format.

---

## features

- detects common SSH clients and remote access tools  
  (putty, termius, remmina, mobaxterm, securecrt, bitvise, etc.)
- detects terminal emulators  
  (kitty, alacritty, wezterm, konsole, windows terminal, powershell, etc.)
- supports:
  - native system binaries
  - flatpak-installed apps (linux)
- offline and fast
- no arguments, no configuration required

---

## supported platforms

- linux
- windows

macos is not supported.

---

## requirements

- python 3.7+
- colorama

install dependency:
```bash
pip install colorama
````

---

## usage

run the script:

```bash
python ssh_belt.py
```

example output:

```
[/] Release/Distro: Arch Linux

[+] RESULTS
[*] Found 'kitty' in '/usr/bin/kitty'
[*] Found 'putty' in '/usr/bin/putty'
[*] Found flatpak package 'termius' in '/var/lib/flatpak/app/com.termius.Termius'
```

---

## how it works

* detects the current operating system
* checks predefined installation paths for known tools
* reports only paths that actually exist
* does not execute or interact with any detected application

---

## disclaimer

* this script is intended for **red team operations**, lab environments, and system enumeration during security assessments
* this is a simple utility and will likely be replaced or rewritten with a more advanced and flexible version in the future
* inspired by the Seatbelt functionality of the [Sliver client](https://sliver.sh/)
---

## limitations

* detection is strictly path-based
  tools installed in custom locations will not be detected
* no version detection
* no macos support

---

## license

use it, modify it, break it. i don't care.

