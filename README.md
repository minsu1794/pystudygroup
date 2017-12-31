# Python Study Group - Documenting our Coding Adventures
## Getting Started
These are the exact steps I used to set up my python workspace on Windows 10. Feel free to use other software if you can figure it out! 
1. Download Git [here](https://git-scm.com/downloads) (I just accepted all default options during the install.)  
_Make sure **"use Git from the Windows Command Prompt"** is selected when the installer asks for path options._
2. Make a GitHub Account [here](https://github.com/)  
3. Download PowerShell [here](https://github.com/powershell/powershell#get-powershell)  
4. Set up Git path:  
* In order to run Git in PowerShell you need to manually give the system the path by navigating as follows:  
  * Control Panel\System and Security\System
  * Advanced System Settings
  * Environmental Variables
    * Scroll down to the 'path' variable and double click it or click edit once 'path' is highlighted
    * Click 'New' and then add the following text 
      * _C:\Program Files (x86)\Git\cmd_  
      * _C:\Program Files (x86)\Git\bin_
  * To test, open powershell and type `git`
    * A usage message should appear
