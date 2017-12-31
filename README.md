# Python Study Group - Documenting our Coding Adventures
## Getting Started
These are the exact steps I used to set up my python workspace on Windows 10. Feel free to use other software if you can figure it out!
1. Download Git [here](https://git-scm.com/downloads) (I just accepted all default options during the install.)  
_Make sure **"use Git from the Windows Command Prompt"** is selected when the installer asks for path options._
2. Make a GitHub Account [here](https://github.com/)  
3. Download PowerShell [here](https://github.com/powershell/powershell#get-powershell)  
4. Configure Git in PowerShell:  
  * In order to run Git in PowerShell you need to manually give the system the path by navigating as follows:  
    * Control Panel\System and Security\System
    * Advanced System Settings
    * Environmental Variables
      * Scroll down to the 'path' variable and double click it or click edit once 'path' is highlighted
      * Click 'New' and then add the following text
        * _C:\Program Files (x86)\Git\cmd_  
        * _C:\Program Files (x86)\Git\bin_
  * To test, open PowerShell and type `git`
    * A usage message should appear
  * Setup username to post commits with:  
 `git config --global user.name "YOURUSERNAME"`
  * Setup email to post commits with:  
`git config --global user.email "email@example.com"`
5. Download Atom [here](https://atom.io/)
6. Download Python 3: Get the 'Windows x86-64 executable installer' [here](https://www.python.org/downloads/windows/)  
_Make sure to tick "Add Python 3.x to Path"_  
  * To test, open PowerShell and type `python --version`  
  _A version message should appear_
7. Download Biopython and Numpy  
  * In PowerShell type `pip install biopython`
  * Successful Installation Message:
~~~~
Collecting biopython
Using cached biopython-1.70-cp36-cp36m-win_amd64.whl
Collecting numpy (from biopython)
Downloading numpy-1.13.3-cp36-none-win_amd64.whl (13.1MB)
100% |████████████████████████████████| 13.1MB 34kB/s
Installing collected packages: numpy, biopython
Successfully installed biopython-1.70 numpy-1.13.3
~~~~
8. Clone the GitHub repository  
  * In PowerShell type:
  ~~~~  
  cd ~/Documents/GitHub  
  git clone https://github.com/tonyhiran/pystudygroup.git
  cd pystudygroup
  git branch YOURUSERNAME
  git checkout YOURUSERNAME
  ~~~~

Now we are (probably) ready to do some coding!
