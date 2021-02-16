import wmi 
import os
import sys
from constants import GAMES

manager = wmi.WMI()

def discover_process(target_process: str):
    for process in manager.Win32_Process():
        if (process.Name == target_process):
            print(f"Discovered {target_process}. running")
            return process 
        print(f"Process name: {target_process} is not running")
        raise ProcessLookupError()

def list_processes():
    process_list = []
    for process in manager.Win32_Process():
        process_list.append(process.Name)
    return process_list

def check_running_programs(target_process_name: str,
                          comparable_processes: list,
                          running_processes: list):
    for element in running_processes:
        if element in comparable_processes:
            print(f"Discovered task: {element}. Attempting to terminate process {target_process_name}")
            shutdown(process_name=target_process_name)
            return
    print("Cannot find queried processes running. Target process will stay alive.")
            
def shutdown(process_name: str):
    if (process_name == "vmmem"):
        os.system(os.system('cmd /k "wsl --shutdown"'))
        print("Issued shutdown command for vmmem process")
    else:
        try: 
            running_process = discover_process(process_name)
            running_process.Terminate()

        except ProcessLookupError as err:
            print(f"Process Not Found. May not be running: {err}")

        except Exception as err:
            print(f"Unknown error occurred. Details {err}")            

# task run definition
if __name__ == "__main__":
    try:
        proc_name = sys.argv[1]
        print(f"Target process name: {proc_name}")
        proc_list = list_processes() 
        check_running_programs(target_process_name=proc_name,
                            comparable_processes=GAMES,
                            running_processes=proc_list)
        exit(0)
    except IndexError as err:
        print(f"IndexError: ensure the process name is passed as launch argument: {err}")
        exit(1)
    except Exception as err:
        print(f"An unknown error has occurred: {err}")
        exit(1)