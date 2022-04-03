### Import Library
import platform
import subprocess
### Define functions - Main stuff
def linux():
    print("Cool stuff")
def windows():
    from urllib.request import urlretrieve
    import getpass
    windowsurl = 'https://download.foldingathome.org/releases/public/release/fah-installer/windows-10-32bit/v7.6/fah-installer_7.6.21_x86.exe'
    print('File Downloading')
    usrname = getpass.getuser()
    destination = f'C:\\Users\\{usrname}\\Downloads\\fah.exe'
    download = urlretrieve(windowsurl, destination)
    print('File downloaded')
    returned_value = subprocess.call(destination, shell=True)  # returns the exit code in unix
    print('returned value:', returned_value)

### Print intro
print(" █▀▀ █▀█ █░░ █▀▄ █ █▄░█ █▀▀ ▄▀█ ▀█▀ █░█ █▀█ █▀▄▀█ █▀▀")
print(" █▀░ █▄█ █▄▄ █▄▀ █ █░▀█ █▄█ █▀█ ░█░ █▀█ █▄█ █░▀░█ ██▄")
print("Folding@Home - Python Edition")
print("Created by Jonte@Jontes.Page")
print("---")
### User Experience
systemType=platform.system()
print("You are using the " + systemType + " version of FAH4PY")
if systemType == "Linux":
    linux()
elif systemType == "Windows":
    windows()
else:
    print("Sorry, this isn't supported. Please use the offical website: https://foldingathome.org/?lng=en#downloads")
