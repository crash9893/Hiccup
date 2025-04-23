import speech_recognition as sr
import subprocess
import os
import winreg
import win32gui
import win32con
import time

class Hiccup:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.running = True
        self.app_paths = {
            'explorer': 'explorer.exe',
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'chrome': 'chrome.exe',
            'firefox': 'firefox.exe',
            'edge': 'msedge.exe',
            'word': 'WINWORD.EXE',
            'excel': 'EXCEL.EXE',
            'powerpoint': 'POWERPNT.EXE',
            'paint': 'mspaint.exe',
            'cmd': 'cmd.exe',
            'terminal': 'wt.exe',
            'settings': 'ms-settings:',
            'control': 'control.exe',
            'task manager': 'taskmgr.exe',
        }

    def listen(self):
        with sr.Microphone() as source:
            print("Say a command (e.g., 'open explorer')...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                return None

    def run(self):
        print("Hiccup is listening! Say 'stop' to quit.")
        print("\nAvailable commands:")
        print("1. 'open <app_name>' - Opens an application")
        print("2. 'close <app_name>' - Closes an application")
        print("3. 'minimize <app_name>' - Minimizes an application")
        print("4. 'maximize <app_name>' - Maximizes an application")
        print("   Supported apps:", ", ".join(sorted(self.app_paths.keys())))
        print("5. 'stop' - Quits the program\n")
        
        while self.running:
            command = self.listen()
            if command:
                if "stop" in command:
                    self.running = False
                    print("Hiccup shutting down.")
                else:
                    self.execute_command(command)

    def find_app_path(self, app_name):
        """Find the application path in the Windows Registry"""
        try:
            # Check common registry locations
            registry_paths = [
                (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths"),
                (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths"),
            ]
            
            for hkey, reg_path in registry_paths:
                try:
                    with winreg.OpenKey(hkey, f"{reg_path}\\{app_name}.exe") as key:
                        path = winreg.QueryValue(key, None)
                        if path:
                            return path
                except WindowsError:
                    continue
                    
            return None
        except Exception as e:
            print(f"Error searching registry: {str(e)}")
            return None
    
    def open_application(self, app_name):
        """Open an application by name"""
        try:
            print(f"Opening application: {app_name}")
            
            # Check if it's a known application
            if app_name in self.app_paths:
                subprocess.Popen(self.app_paths[app_name])
                print(f"Successfully opened {app_name}")
                return
                
            # Try to find the application in the registry
            app_path = self.find_app_path(app_name)
            if app_path:
                subprocess.Popen(app_path)
                print(f"Successfully opened {app_name}")
                return
                
            # Try to find the application in common locations
            common_paths = [
                os.path.join(os.environ.get("ProgramFiles", ""), app_name + ".exe"),
                os.path.join(os.environ.get("ProgramFiles(x86)", ""), app_name + ".exe"),
                os.path.join(os.environ.get("LOCALAPPDATA", ""), app_name + ".exe"),
                os.path.join(os.environ.get("APPDATA", ""), app_name + ".exe"),
            ]
            
            for path in common_paths:
                if os.path.exists(path):
                    subprocess.Popen(path)
                    print(f"Successfully opened {app_name}")
                    return
                    
            print(f"Could not find application: {app_name}")
        except Exception as e:
            print(f"Error opening application: {str(e)}")

    def find_window_by_title(self, app_name):
        """Find a window handle by application name"""
        def callback(hwnd, windows):
            if win32gui.IsWindowVisible(hwnd):
                window_title = win32gui.GetWindowText(hwnd)
                if app_name.lower() in window_title.lower():
                    windows.append(hwnd)
            return True
        
        windows = []
        win32gui.EnumWindows(callback, windows)
        return windows[0] if windows else None

    def close_application(self, app_name):
        """Close an application by name"""
        try:
            hwnd = self.find_window_by_title(app_name)
            if hwnd:
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                print(f"Sent close command to {app_name}")
            else:
                print(f"Could not find window for {app_name}")
        except Exception as e:
            print(f"Error closing application: {str(e)}")

    def minimize_application(self, app_name):
        """Minimize an application by name"""
        try:
            hwnd = self.find_window_by_title(app_name)
            if hwnd:
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
                print(f"Minimized {app_name}")
            else:
                print(f"Could not find window for {app_name}")
        except Exception as e:
            print(f"Error minimizing application: {str(e)}")

    def maximize_application(self, app_name):
        """Maximize an application by name"""
        try:
            hwnd = self.find_window_by_title(app_name)
            if hwnd:
                win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
                print(f"Maximized {app_name}")
            else:
                print(f"Could not find window for {app_name}")
        except Exception as e:
            print(f"Error maximizing application: {str(e)}")

    def execute_command(self, command):
        print(f"Processing: {command}")
        
        # Parse the command
        parts = command.split()
        
        if len(parts) < 2:
            print("Invalid command format")
            return

        action = parts[0].lower()
        app_name = " ".join(parts[1:]).lower()

        if action == "open":
            self.open_application(app_name)
        elif action == "close":
            self.close_application(app_name)
        elif action == "minimize":
            self.minimize_application(app_name)
        elif action == "maximize":
            self.maximize_application(app_name)
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    hiccup = Hiccup()
    hiccup.run()