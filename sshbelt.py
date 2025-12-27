import os
import platform
import colorama
from colorama import Fore
colorama.init() 
red = Fore.RED
white = Fore.WHITE
green = Fore.GREEN
blue = Fore.LIGHTBLUE_EX
yellow = Fore.LIGHTYELLOW_EX
bluee = Fore.CYAN
plat=platform.system()
userg = os.getlogin()


def distro_or_release():
    if plat == "Linux":
        with open('/etc/os-release', 'r') as f:
            dirty_distro = f.readline()
            cleaned = dirty_distro.split('=', 1)[1].strip().strip('"')
        return cleaned
    if plat == "Windows":
        return plat      



linux_paths = {
    # ! === SSH Clients (CLI + GUI) ===
    "putty": "/usr/bin/putty",
    "termius": "/usr/bin/termius",
    "remmina": "/usr/bin/remmina",
    "x2goclient": "/usr/bin/x2goclient",
    "mosh": "/usr/bin/mosh",
    "autossh": "/usr/bin/autossh",
    "byobu": "/usr/bin/byobu",
    # ! === Terminals ===
    "gnome_terminal": "/usr/bin/gnome-terminal",
    "konsole": "/usr/bin/konsole",
    "terminator": "/usr/bin/terminator",
    "tilix": "/usr/bin/tilix",
    "alacritty": "/usr/bin/alacritty",
    "kitty": "/usr/bin/kitty",
    "wezterm": "/usr/bin/wezterm",
    "xterm": "/usr/bin/xterm",
    "xfce4_terminal": "/usr/bin/xfce4-terminal",
    "lxterminal": "/usr/bin/lxterminal",
    "terminus": "/usr/bin/terminus",
    "tabby": "/usr/bin/tabby",
    # ! === RDP / VNC / Remote Access ===
    "vinagre": "/usr/bin/vinagre",
    "rdesktop": "/usr/bin/rdesktop",
    "xfreerdp": "/usr/bin/xfreerdp",
    "nomachine": "/usr/bin/nomachine",
    "chrome_remote_desktop": "/opt/google/chrome-remote-desktop/chrome-remote-desktop",
    "guacamole_client": "/usr/bin/guacamole-client",
}

linux_flatpak_paths = {
    "putty": "/var/lib/flatpak/app/uk.org.greenend.chiark.sgtatham.putty",
    "easyssh": "/var/lib/flatpak/app/com.github.muriloventuroso.easyssh",
    "termius": "/var/lib/flatpak/app/com.termius.Termius",
    "remmina": "/var/lib/flatpak/app/org.remmina.Remmina",
    "ssh_mitm": "/var/lib/flatpak/app/at.ssh_mitm.server",
    "muon": "/var/lib/flatpak/app/io.github.subhra74.Muon",
    "finalshell": "/var/lib/flatpak/app/com.hostbuf.FinalShell",
}



windows_paths = {
    "putty": "C:\\Program Files\\PuTTY\\putty.exe",
    "mobaxterm": "C:\\Program Files (x86)\\Mobatek\\MobaXterm\\MobaXterm.exe",
    "securecrt": "C:\\Program Files\\VanDyke Software\\SecureCRT\\SecureCRT.exe",
    "bitvise": "C:\\Program Files\\Bitvise SSH Client\\BvSsh.exe",
    "kitty": "C:\\Program Files\\KiTTY\\kitty.exe",
    "solar_putty": f"C:\\Users\\{userg}\\AppData\\Local\\SolarWinds\\Solar-PuTTY.exe",
    "mremoteng": "C:\\Program Files (x86)\\mRemoteNG\\mRemoteNG.exe",
    "zoc": "C:\\Program Files (x86)\\ZOC7\\zoc.exe",
    "tabby": f"C:\\Users\\{userg}\\AppData\\Local\\Programs\\Tabby\\Tabby.exe",
    "terminus": f"C:\\Users\\{userg}\\AppData\\Local\\Programs\\Terminus\\Terminus.exe",
    "superputty": "C:\\Program Files\\SuperPuTTY\\SuperPutty.exe",
    "teraterm": "C:\\Program Files (x86)\\teraterm\\ttermpro.exe",
    "remote_desktop_manager": "C:\\Program Files (x86)\\Devolutions\\Remote Desktop Manager\\RemoteDesktopManager.exe",
    "royalts": "C:\\Program Files\\Royal TS V6\\RoyalTS.exe",
    "teleport_connect": "C:\\Program Files\\Teleport\\TeleportConnect.exe",
    "windows_terminal": "C:\\Program Files\\WindowsApps\\Microsoft.WindowsTerminal*",
    "pageant": "C:\\Program Files\\PuTTY\\pageant.exe",
    "pscp_psftp": "C:\\Program Files\\PuTTY\\pscp.exe",
    "xshell": "C:\\Program Files\\NetSarang\\Xshell 7\\Xshell.exe",
    "termius": f"C:\\Users\\{userg}\\AppData\\Local\\Programs\\Termius\\Termius.exe",
    "alacritty": f"C:\\Users\\{userg}\\AppData\\Local\\Microsoft\\WindowsApps\\alacritty.exe",
    "wezterm": f"C:\\Users\\{userg}\\AppData\\Local\\wezterm\\wezterm.exe",
    "hyper": f"C:\\Users\\{userg}\\AppData\\Local\\hyper\\Hyper.exe",
    "cmder": "C:\\tools\\cmder\\Cmder.exe",
    "conemu": "C:\\Program Files\\ConEmu\\ConEmu64.exe",
    "powershell_core": "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
    "mobaterm_home": f"C:\\Users\\{userg}\\Documents\\MobaXterm\\MobaXterm.exe",
    "smartty": r"C:\\Program Files\\SmarTTY\\SmarTTY.exe",
}


ascii = f"""
{blue}[{white}/{blue}]{white} Release/Distro: {yellow}{distro_or_release()} 
                          
{green}[{white}+{green}]{white} RESULTS
"""
print(ascii)



if plat == "Windows":
    for wname, wpath in windows_paths.items():
        if os.path.exists(wpath):
            print(f"{green}[{white}*{green}]{white} Found '{bluee}{wname}{white}' in '{bluee}{wpath}{white}'")

elif plat == "Linux":
    for lname, lpath, in linux_paths.items():
        if os.path.exists(lpath):
            print(f"{green}[{white}*{green}]{white} Found '{bluee}{lname}{white}' in '{bluee}{lpath}{white}'")
    for lfname, lfpath, in linux_flatpak_paths.items():
        if os.path.exists(lfpath):
            print(f"{green}[{white}*{green}]{white} Found flatpak package '{bluee}{lfname}{white}' in '{bluee}{lfpath}{white}'")        
elif plat != "Linux" or "Windows":
    print("[-]Platform not supported.")
print("\n")
