# Python Study Group - Documenting our Coding Adventures
## Table of Contents
* [Getting Started](#getting-started)
* [Programming Exercises](#programming-exercises)  
  * [Program 1: Hello, World](#program-1-hello-world)
  * [Program 2: Brute Force Optimize](#program-2-brute-force-optimize)
* [References and Additional Resources](References.md#references)
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
  * To figure out which email to use, go to [Primary email address](https://github.com/settings/emails)
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
  cd ~/Documents/
  mkdir GitHub
  cd GitHub
  git clone https://github.com/tonyhiran/pystudygroup.git
  cd pystudygroup
  git branch YOURUSERNAME
  git checkout YOURUSERNAME
  ~~~~

Now we are (probably) ready to do some coding!

## Programming Exercises
### Program 1: Hello, World  
> _"The 'Hello World' example is the traditional incantation to the programming gods and will ensure your quick mastery of the language, so please make sure you actually do this exercise, instead of just reading about it."_- Simon Cozens, Beginning Perl    

#### Skills Gained
* Print Statements
* Shell Commands: cd, mkdir
* Git Commands: status, add, commit, push

#### Implementation
1. In **PowerShell** type the following to make your personal folder and switch to it:
~~~~
cd ~/Documents/GitHub/pystudygroup
mkdir "YOURUSERNAME"
cd YOURUSERNAME
~~~~
2. Similarly, make the Hello World folder:
~~~~
mkdir "Program1"
cd "Program1"
~~~~
3. In **Atom** make a file named "`Hello World.py`" with the following contents:
~~~~
#!/usr/bin/env python3
print("Hello, World!");
~~~~
4. In **PowerShell** type `python "Hello World.py"`  
5. Assuming things went well, commit and push changes to GitHub
~~~~
git status
git add .
git commit -m "Added Hello World.py"
git push
~~~~

Now you have been blessed by the programming gods.

### Program 2: Brute Force Optimize
Writing this program plunges you into the world of python!
#### Skills Gained
* Variables: float, string, int
* Reading user input
* If Statements
* While loops
* For loops
* Lists
* Optional: error handling

#### Specifications
* Create a program which solves a 2-dimensional optimization problem  
  * The problem will be in the following form:  
    * min/max f(x,y)
    * st. g<sub>1</sub>(x, y), g<sub>2</sub>(x, y), ... , g<sub>n</sub>(x, y) conditions satisfied
    * x<sub>lb</sub> &le; x &le; x<sub>ub</sub>
    * y<sub>lb</sub> &le; y &le; y<sub>ub</sub>
  * And the program will check all possible values of x and y before outputting the optimal solution
    * x values checked: x<sub>lb</sub>, x<sub>lb</sub> + i, x<sub>lb</sub> + 2i, ... , x<sub>ub</sub> - i, x<sub>ub</sub>
    * y values checked: y<sub>lb</sub>, y<sub>lb</sub> + j, y<sub>lb</sub> + 2j, ... , y<sub>ub</sub> - j, x<sub>ub</sub>
      * i is x increment, j is y increment


* User input (read in from command line)
  * Optimization type (min or max)
  * Objective function eg. x\*\*2 + 4\*x\*y + 4y\*\*2
  * Constraints: eg. x &ge; 0, math.sin(y) > x
  * x lower bound, upper bound, increment
  * y lower bound, y upper bound, y increment


* Output
  * Optimal objective function value
  * Solution: (x, y)

#### Implementation Hints
> Try to code it one step at a time!  
_Spoilers_: See my version at branch [TonyHiran](https://github.com/tonyhiran/pystudygroup/tree/TonyHiran/TonyHiran/Program2)

* To import some useful functions:
~~~~
import math
import numpy
import sys
~~~~
* Common math symbols/functions in python:
~~~~
add:          +
subtract:     -
multiply:     *
divide:       /
floor divide: //
modulo:       %
exponent:     **
sqrt:         math.sqrt(expr)
log:          math.log(x, base)
sin:          math.sin(expr)
cos:          math.cos(expr)
tan:          math.tan(expr)
e:            math.e
π:            math.pi
~~~~
* Getting input:
  * `string_var = input("PROMPT USER FOR STRING INPUT")`
  * `float_var  =  float(input("PROMPT USER FOR NUMERIC INPUT"))`

* Lists:
  * Initializing new list
  ~~~~
  empty_list = []
  int_list = [1, 2, 3, 4, 5]
  mixed_list = [1, 'two', 3.1]
  ~~~~
  * Useful List functions
    * append()
    * insert()
    * sort()
    * len()
    * _See [references](References.md#program2-brute-opti) for more_
* If Statements
~~~~
if(expression):
    PERFORM ACTIONS
elif(expression):
    PERFORM ACTIONS
else:
    PERFORM DEFAULT ACTIONS
~~~~
  * Note that each code block has to be indented to be under the relevant conditions  
* While loops
~~~~
while CONDITION:
    PERFORM ACTIONS
~~~~
* For loops
~~~~
for i in LIST
    PERFORM ACTIONS
~~~~
example:
~~~~
for i in numpy.arange(0,10)
    print(i)
~~~~
* Evaluate expression from string
~~~~
eval(string_expr)
~~~~
Example:
~~~~
x = 1
f_x=eval(x**2 + 2*x + 1)
print(f_x)
~~~~
  * Note: eval can be dangerous because
    1. It is compiled as the code runs so it can slow things down
    2. Makes debugging difficult if you use it to run certain commands  
    3. It allows the user to make your program execute any command (malicious code injection threat)
  * There are other functions that can be used instead
  * You can also have conditions to make sure the eval statement inputs are 'sanitized'
  * Here we are just using it ourselves to input strings of math expressions, so it's ok.   


* Optional: Output custom error message after incorrect input
  * `print('invalid input')`
  * `sys.exit(1)`


_More coming soon!_  
