# Task Killer #

## Introduction ## 
This project was inspired as a workaround for terminating the `vmmem` process at a regular interval in order to prevent it from interrupting unrelated workflows. The gist is that when working under WSL, the Linux side of the house attempts to take dominion of instance memory it doesn't necessarily need. This presents a problem when doing things that are memory intensive. When this happens, the memory is no longer available to Windows, but it's exposed via the `vmmem` task in Task Manager. Unfortunately, this task cannot be shutdown from Windows as its technically not owned by Windows, but it CAN be shutdown via the `wsl --shutdown` command in the terminal. Enter **Task Killer**, the solution that allows for automating this shutdown task, along with any standard task you just want killed when other programs are running. Simply put, when Task Killer finds a defined, no longer needed program running against a list of other programs, it kills it. In addition, this can be automated with the Windows Task Scheduler and the included batch file. 


## Prerequisites ##
- Python 3
- Windows
## Getting Started ## 

- Define what programs you want evaluated by editing the `PROGRAMS_LIST` in the `constants.py` file. A sample list is left there for reference.
- In the root of the project create a Python virtual environment in a directory named `.venv` by pasting the command in the terminal:
    ``` python -m venv .venv ```
- Install dependencies by running:
    ``` pip install -r requirements.txt```

- Run the file in the terminal and pass the process you want terminated as an argument:
``` python task_killer.py <process name here> ```






