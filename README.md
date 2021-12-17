# SETTING UP YOUR ENVIRONMENT

Welcome to GOA's CS2: Analyzing Data with Python course!
Congratulations on accepting your first assignment.

---

## REQUIRED PROGRAMS

We'll be using Visual Studio Code as our IDE for this course. You can download it at this website:
https://code.visualstudio.com/

We'll also be using Github Classroom. You should have already [signed up for Github](https://github.com/)
and accepted your first assignment if you are reading this!

You'll need the following programs and extensions for VS Code to be able to work with Python.



> ### WINDOWS
> * Additional Programs
>     * [Python (from the Microsoft Store)](https://www.microsoft.com/en-us/p/python-310/9pjpw5ldxlz5)
> * [VS Code Extensions](https://code.visualstudio.com/docs/introvideos/extend)
>     * Python (in addition to the install from the Microsoft Store)
>     * Github Classroom
>         * Sign in with your [Github](https://github.com/) account!


> ### MACOS
> * Additional Programs
>     * [Python (from Python.org)](https://www.python.org)
> * [VS Code Extensions](https://code.visualstudio.com/docs/introvideos/extend)
>     * Python (in addition to the install from the Microsoft Store)
>     * Github Classroom
>         * Sign in with your [Github](https://github.com/) account!

---

## PYTHON MODULES

You will receive additional instructions on installing the Python modules we'll be using in this course
as we add them to our repertoire.

However, if you'd like to give it a shot to see what our `sample.py` program can do, here are the instructions! 

The most important steps are <ins>underlined</ins>.


> ### WINDOWS
> 1. <ins>Open the Terminal</ins>
>     * At the top of the VSCode window, you'll see the Terminal menu in the menu bar. 
Choose `New Terminal` from the menu, or use the shortcut `Ctrl` + `Shift` + \`
> 2. Create a virtual environment
>     * <ins>In the Terminal, type `Python -m venv venv`</ins>
>         * This creates a new folder called `venv`
>         * The purpose of this folder is to have only the Python modules we need in our program.
> 3. Activate the virtual environment
>     * <ins>In the Terminal, type `Set-ExecutionPolicy -ExecutionPolicy remoteSigned -Scope Process`</ins>
>         * This gives our program permission to install modules in the virtual environment
>     * <ins>In the Terminal, type `.\venv\Scripts\activate`
>         * You'll see that the Terminal prompt changes to include `(venv)` at the beginning of the prompt. That's how you know you're in the right environment.
> 4. Install the required package(s)
>     * <ins>In the Terminal, type `pip install bokeh`</ins>
>     * Bokeh is the package used for this visualization
> 5. Run the program
>     * Select the sample.py file in the explorer
>         * If you don't see the file list, click on the icon on the top left of the window
>     * Click the play button on the top right of the window


> ### MACOS
> 1. <ins>Open the Terminal</ins>
>     * In the menu bar at the top of your screen, you'should see the Terminal menu. Choose `New Terminal` from the menu, or use the shortcut `Ctrl` + `Shift` + \`
> 2. Create a virtual environment
>     * <ins>In the Terminal, type `python3 -m venv venv`</ins>
>         * This creates a new folder called `venv`
>         * The purpose of this folder is to have only the Python modules we need in our program.
> 3. Activate the virtual environment
>     * <ins>In the Terminal, type `venv/bin/activate`
>         * You'll see that the Terminal prompt changes to include `(venv)` at the beginning of the prompt. That's how you know you're in the right environment.
> 4. Install the required package(s)
>     * <ins>In the Terminal, type `pip install bokeh`</ins>
>     * Bokeh is the package used for this visualization
> 5. Run the program
>     * Select the sample.py file in the explorer
>         * If you don't see the file list, click on the icon on the top left of the window
>     * Click the play button on the top right of the window