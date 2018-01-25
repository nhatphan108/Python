import ctypes, sys
import os
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def run_as_admin(program):
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, program, None, 1)

def execute():
    try:
        os.system("taskkill /f /im pythonw.exe")
    except:
        pass

    os.startfile("WebsiteBlocker.pyw")
if __name__ == "__main__":
    execute()
