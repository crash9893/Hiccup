import speech_recognition as sr
import subprocess
import os
import winreg
import win32gui
import win32con
import time
import re
from urllib.parse import urlparse
from terminator import Desktop
from PIL import Image
import numpy as np

class Hiccup:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.running = True
        self.desktop = Desktop()
        self.app_paths = {
            # System and File Management
            'explorer': 'explorer.exe',
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'cmd': 'cmd.exe',
            'terminal': 'wt.exe',
            'settings': 'ms-settings:',
            'control': 'control.exe',
            'task manager': 'taskmgr.exe',
            
            # Web Browsers
            'chrome': 'chrome.exe',
            'firefox': 'firefox.exe',
            'edge': 'msedge.exe',
            'brave': 'brave.exe',
            'opera': 'opera.exe',
            
            # Microsoft Office
            'word': 'WINWORD.EXE',
            'excel': 'EXCEL.EXE',
            'powerpoint': 'POWERPNT.EXE',
            'outlook': 'OUTLOOK.EXE',
            'access': 'MSACCESS.EXE',
            'publisher': 'MSPUB.EXE',
            'visio': 'VISIO.EXE',
            'project': 'WINPROJ.EXE',
            
            # Code Editors and IDEs
            'vscode': 'code.exe',
            'visual studio': 'devenv.exe',
            'visual studio code': 'code.exe',
            'sublime': 'sublime_text.exe',
            'notepad++': 'notepad++.exe',
            'atom': 'atom.exe',
            'intellij': 'idea64.exe',
            'pycharm': 'pycharm64.exe',
            'webstorm': 'webstorm64.exe',
            'phpstorm': 'phpstorm64.exe',
            'rider': 'rider64.exe',
            'clion': 'clion64.exe',
            'eclipse': 'eclipse.exe',
            'netbeans': 'netbeans64.exe',
            'android studio': 'studio64.exe',
            'xcode': 'Xcode.exe',
            
            # Version Control
            'git': 'git.exe',
            'github desktop': 'GitHubDesktop.exe',
            'gitkraken': 'GitKraken.exe',
            'sourcetree': 'SourceTree.exe',
            'tortoisegit': 'TortoiseGitProc.exe',
            
            # Database Tools
            'sql server': 'ssms.exe',
            'mysql workbench': 'MySQLWorkbench.exe',
            'postgresql': 'pgAdmin4.exe',
            'mongodb': 'MongoDBCompass.exe',
            'dbeaver': 'dbeaver.exe',
            'datagrip': 'datagrip64.exe',
            
            # API and Network Tools
            'postman': 'Postman.exe',
            'insomnia': 'Insomnia.exe',
            'wireshark': 'Wireshark.exe',
            'fiddler': 'Fiddler.exe',
            'charles': 'Charles.exe',
            
            # Container and Virtualization
            'docker': 'Docker Desktop.exe',
            'virtualbox': 'VirtualBox.exe',
            'vmware': 'vmware.exe',
            'kubernetes': 'kubectl.exe',
            
            # Design Tools
            'figma': 'Figma.exe',
            'adobe xd': 'Adobe XD.exe',
            'photoshop': 'Photoshop.exe',
            'illustrator': 'Illustrator.exe',
            'sketch': 'Sketch.exe',
            'invision': 'InVision Studio.exe',
            
            # Terminal and Shell
            'powershell': 'powershell.exe',
            'bash': 'bash.exe',
            'wsl': 'wsl.exe',
            'cygwin': 'cygwin.exe',
            'putty': 'putty.exe',
            
            # Utility Tools
            'paint': 'mspaint.exe',
            'snipping tool': 'SnippingTool.exe',
            'snip and sketch': 'ScreenSketch.exe',
            'remote desktop': 'mstsc.exe',
            'teamviewer': 'TeamViewer.exe',
            'discord': 'Discord.exe',
            'slack': 'Slack.exe',
            'teams': 'Teams.exe',
            'zoom': 'Zoom.exe',
            'skype': 'Skype.exe',
        }
        
        # Common website mappings
        self.website_mappings = {
            'google': 'https://www.google.com',
            'youtube': 'https://www.youtube.com',
            'facebook': 'https://www.facebook.com',
            'twitter': 'https://www.twitter.com',
            'github': 'https://www.github.com',
            'bing': 'https://www.bing.com',
            'amazon': 'https://www.amazon.com',
            'netflix': 'https://www.netflix.com',
            'linkedin': 'https://www.linkedin.com',
            'reddit': 'https://www.reddit.com',
            'stackoverflow': 'https://stackoverflow.com',
            'medium': 'https://medium.com',
            'dev.to': 'https://dev.to',
            'gitlab': 'https://gitlab.com',
            'bitbucket': 'https://bitbucket.org',
            'npm': 'https://www.npmjs.com',
            'docker hub': 'https://hub.docker.com',
            'kubernetes': 'https://kubernetes.io',
            'microsoft docs': 'https://docs.microsoft.com',
            'python docs': 'https://docs.python.org',
            'rust docs': 'https://doc.rust-lang.org',
            'mdn': 'https://developer.mozilla.org',
            'w3schools': 'https://www.w3schools.com',
            'coursera': 'https://www.coursera.org',
            'udemy': 'https://www.udemy.com',
            'pluralsight': 'https://www.pluralsight.com',
            'leetcode': 'https://leetcode.com',
            'hackerrank': 'https://www.hackerrank.com',
            'codecademy': 'https://www.codecademy.com',
            'freecodecamp': 'https://www.freecodecamp.org',
        }

        # Get the user's desktop path
        self.desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

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
        print("\nYou can use natural language to give commands. Here are some examples:")
        print("\nApplication Commands:")
        print("- 'open chrome' - Opens Chrome browser")
        print("- 'close notepad' - Closes Notepad")
        print("- 'minimize word' - Minimizes Microsoft Word")
        print("- 'maximize excel' - Maximizes Microsoft Excel")
        
        print("\nWebsite Commands:")
        print("- 'open google in chrome' - Opens Google in Chrome")
        print("- 'visit github using firefox' - Opens GitHub in Firefox")
        print("- 'go to youtube in edge' - Opens YouTube in Edge")
        
        print("\nFile Management Commands:")
        print("- 'create a folder named projects on desktop' - Creates a folder")
        print("- 'make a directory called documents in downloads' - Creates a folder")
        print("- 'delete file test.txt from desktop' - Deletes a file")
        print("- 'remove the file old.txt in documents' - Deletes a file")
        
        print("\nYou can be flexible with your wording. For example:")
        print("- 'please create a folder named work on my desktop'")
        print("- 'could you delete the file notes.txt from documents'")
        print("- 'I want to open google in chrome'")
        print("- 'show me github using firefox'")
        
        print("\nSupported applications by category:")
        categories = {}
        for app in sorted(self.app_paths.keys()):
            # Determine category based on app name
            category = "Other"
            if any(browser in app for browser in ['chrome', 'firefox', 'edge', 'brave', 'opera']):
                category = "Web Browsers"
            elif any(ide in app for ide in ['vscode', 'visual studio', 'sublime', 'notepad++', 'atom', 'intellij', 'pycharm', 'webstorm', 'phpstorm', 'rider', 'clion', 'eclipse', 'netbeans', 'android studio', 'xcode']):
                category = "Code Editors and IDEs"
            elif any(office in app for office in ['word', 'excel', 'powerpoint', 'outlook', 'access', 'publisher', 'visio', 'project']):
                category = "Microsoft Office"
            elif any(vc in app for vc in ['git', 'github', 'gitkraken', 'sourcetree', 'tortoisegit']):
                category = "Version Control"
            elif any(db in app for db in ['sql', 'mysql', 'postgresql', 'mongodb', 'dbeaver', 'datagrip']):
                category = "Database Tools"
            elif any(api in app for api in ['postman', 'insomnia', 'wireshark', 'fiddler', 'charles']):
                category = "API and Network Tools"
            elif any(container in app for container in ['docker', 'virtualbox', 'vmware', 'kubernetes']):
                category = "Container and Virtualization"
            elif any(design in app for design in ['figma', 'adobe', 'photoshop', 'illustrator', 'sketch', 'invision']):
                category = "Design Tools"
            elif any(term in app for term in ['powershell', 'bash', 'wsl', 'cygwin', 'putty', 'cmd', 'terminal']):
                category = "Terminal and Shell"
            elif any(sys in app for sys in ['explorer', 'settings', 'control', 'task manager']):
                category = "System and File Management"
            elif any(util in app for util in ['paint', 'snipping', 'remote desktop', 'teamviewer', 'discord', 'slack', 'teams', 'zoom', 'skype']):
                category = "Utility Tools"
            
            if category not in categories:
                categories[category] = []
            categories[category].append(app)
        
        # Print categories and apps
        for category, apps in sorted(categories.items()):
            print(f"\n{category}:")
            for app in sorted(apps):
                print(f"  - {app}")
        
        print("\nSupported websites:")
        for website in sorted(self.website_mappings.keys()):
            print(f"  - {website}")
        
        print("\nSupported browsers: chrome, firefox, edge, brave, opera")
        
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

    def is_url_command(self, parts):
        """Check if the command is a URL command"""
        if len(parts) < 3:
            return False
            
        # Convert all parts to lowercase for easier matching
        lower_parts = [p.lower() for p in parts]
        command_text = " ".join(lower_parts)
        
        # Check for open keywords
        open_keywords = ["open", "launch", "go to", "navigate to", "visit", "show me"]
        
        # Check for browser keywords
        browser_keywords = ["in", "using", "with", "via", "through"]
        
        # Check if the command contains an open keyword and a browser keyword
        for open_keyword in open_keywords:
            if open_keyword in command_text:
                for browser_keyword in browser_keywords:
                    if browser_keyword in command_text:
                        return True
        
        return False

    def parse_url_command(self, parts):
        """Parse a URL command into website and browser"""
        try:
            # Convert all parts to lowercase for easier matching
            lower_parts = [p.lower() for p in parts]
            
            # Find the browser keyword
            browser_keywords = ["in", "using", "with", "via", "through"]
            browser_keyword = None
            browser_index = -1
            
            for keyword in browser_keywords:
                if keyword in lower_parts:
                    browser_keyword = keyword
                    browser_index = lower_parts.index(keyword)
                    break
            
            if browser_index < 1:
                return None, None
            
            # Find the open keyword
            open_keywords = ["open", "launch", "go to", "navigate to", "visit", "show me"]
            open_index = -1
            
            for keyword in open_keywords:
                if keyword in lower_parts:
                    open_index = lower_parts.index(keyword)
                    break
            
            if open_index < 0:
                return None, None
            
            # Get the website part (everything between open keyword and browser keyword)
            website = " ".join(parts[open_index + 1:browser_index]).lower()
            
            # Get the browser part (everything after browser keyword)
            browser = " ".join(parts[browser_index + 1:]).lower()
            
            return website, browser
        except (ValueError, IndexError):
            return None, None

    def get_full_url(self, website):
        """Convert a website name to a full URL"""
        # If it's already a URL, return it
        if website.startswith(('http://', 'https://')):
            return website
            
        # Check if it's in our mappings
        if website in self.website_mappings:
            return self.website_mappings[website]
            
        # If it looks like a domain, add https://
        if '.' in website and not website.startswith(('http://', 'https://')):
            return f'https://{website}'
            
        # If it's a search term, use Google
        return f'https://www.google.com/search?q={website}'

    def open_url(self, website, browser=None):
        """Open a URL in the specified browser"""
        try:
            url = self.get_full_url(website)
            print(f"Opening URL: {url}")
            
            if browser:
                # Check if the browser is supported
                if browser not in ['chrome', 'firefox', 'edge']:
                    print(f"Unsupported browser: {browser}")
                    print("Falling back to default browser")
                    browser = None
            
            # Use the terminator module to open the URL
            self.desktop.open_url(url, browser)
            print(f"Successfully opened {url}")
            
        except Exception as e:
            print(f"Error opening URL: {str(e)}")

    def is_file_management_command(self, parts):
        """Check if the command is a file management command"""
        if len(parts) < 2:
            return False
            
        # Convert all parts to lowercase for easier matching
        lower_parts = [p.lower() for p in parts]
        command_text = " ".join(lower_parts)
        
        # Check for create/make folder commands
        create_keywords = ["create", "make", "please create", "could you create", "can you create", 
                          "i want to create", "i need to create", "i would like to create", "new"]
        
        folder_keywords = ["folder", "directory", "folder named", "folder called", "folder with name", 
                          "folder on", "folder in", "folder at", "folder to"]
        
        # Check if the command contains a create keyword and a folder keyword
        for create_keyword in create_keywords:
            if create_keyword in command_text:
                for folder_keyword in folder_keywords:
                    if folder_keyword in command_text:
                        return True
        
        # Check for delete/remove file commands
        delete_keywords = ["delete", "remove", "please delete", "could you delete", "can you delete", 
                          "i want to delete", "i need to delete", "i would like to delete", "erase"]
        
        file_keywords = ["file", "the file", "my file", "the file named", "the file called", 
                        "file on", "file in", "file at", "file to"]
        
        # Check if the command contains a delete keyword and a file keyword
        for delete_keyword in delete_keywords:
            if delete_keyword in command_text:
                for file_keyword in file_keywords:
                    if file_keyword in command_text:
                        return True
        
        return False

    def parse_file_management_command(self, parts):
        """Parse a file management command and return the action, type, location, and name"""
        # Convert all parts to lowercase for easier matching
        lower_parts = [p.lower() for p in parts]
        command_text = " ".join(lower_parts)
        
        # Initialize variables
        action = None
        item_type = None
        location = "desktop"  # Default to desktop
        name = None
        
        # Determine action and item type
        create_keywords = ["create", "make", "new"]
        delete_keywords = ["delete", "remove", "erase"]
        
        # Check for create/make folder commands
        if any(keyword in command_text for keyword in create_keywords):
            action = "create"
            item_type = "folder"
            
            # Find the folder name
            # Look for "named" or "called" keywords
            name_keywords = ["named", "called", "with", "as", "name"]
            for keyword in name_keywords:
                if keyword in lower_parts:
                    keyword_index = lower_parts.index(keyword)
                    if keyword_index + 1 < len(parts):
                        # Get all parts after the keyword
                        name = " ".join(parts[keyword_index + 1:])
                        break
            
            # If no name found, look for "folder" keyword and take the next word
            if not name and "folder" in lower_parts:
                folder_index = lower_parts.index("folder")
                if folder_index + 1 < len(parts):
                    # Get all parts after "folder"
                    name = " ".join(parts[folder_index + 1:])
            
            # If still no name, take everything after the action
            if not name:
                # Find the first action keyword
                for keyword in create_keywords:
                    if keyword in lower_parts:
                        action_index = lower_parts.index(keyword)
                        if action_index + 1 < len(parts):
                            # Get all parts after the action
                            name = " ".join(parts[action_index + 1:])
                            break
            
            # Look for location indicators
            location_keywords = ["on", "in", "at", "to", "from"]
            for keyword in location_keywords:
                if keyword in lower_parts:
                    keyword_index = lower_parts.index(keyword)
                    if keyword_index + 1 < len(parts):
                        # Check if the next word is a location
                        potential_location = parts[keyword_index + 1].lower()
                        if potential_location in ["desktop", "documents", "downloads", "pictures", "music", "videos"]:
                            location = potential_location
                            # If we found a location, remove it from the name
                            if name:
                                # Create a list of words to remove
                                words_to_remove = []
                                name_parts = name.split()
                                for i, part in enumerate(name_parts):
                                    if part.lower() == potential_location:
                                        words_to_remove.append(i)
                                # Remove the words in reverse order to maintain indices
                                for i in reversed(words_to_remove):
                                    name_parts.pop(i)
                                name = " ".join(name_parts)
                            break
        
        # Check for delete/remove file commands
        elif any(keyword in command_text for keyword in delete_keywords):
            action = "delete"
            item_type = "file"
            
            # Find the file name
            # Look for "file" keyword and take the next word
            if "file" in lower_parts:
                file_index = lower_parts.index("file")
                if file_index + 1 < len(parts):
                    # Check if the next part is a location indicator
                    next_part = parts[file_index + 1].lower()
                    if next_part in ["on", "in", "at", "to", "from"]:
                        # Skip the location indicator and take the next word
                        if file_index + 2 < len(parts):
                            name = " ".join(parts[file_index + 2:])
                    else:
                        # Get all parts after "file"
                        name = " ".join(parts[file_index + 1:])
            
            # If no name found, take everything after the action
            if not name:
                # Find the first action keyword
                for keyword in delete_keywords:
                    if keyword in lower_parts:
                        action_index = lower_parts.index(keyword)
                        if action_index + 1 < len(parts):
                            # Get all parts after the action
                            name = " ".join(parts[action_index + 1:])
                            break
            
            # Look for location indicators
            location_keywords = ["on", "in", "at", "to", "from"]
            for keyword in location_keywords:
                if keyword in lower_parts:
                    keyword_index = lower_parts.index(keyword)
                    if keyword_index + 1 < len(parts):
                        # Check if the next word is a location
                        potential_location = parts[keyword_index + 1].lower()
                        if potential_location in ["desktop", "documents", "downloads", "pictures", "music", "videos"]:
                            location = potential_location
                            # If we found a location, remove it from the name
                            if name:
                                # Create a list of words to remove
                                words_to_remove = []
                                name_parts = name.split()
                                for i, part in enumerate(name_parts):
                                    if part.lower() == potential_location:
                                        words_to_remove.append(i)
                                # Remove the words in reverse order to maintain indices
                                for i in reversed(words_to_remove):
                                    name_parts.pop(i)
                                name = " ".join(name_parts)
                            break
        
        # Clean up the name
        if name:
            # Create a list of words to remove
            words_to_remove = []
            name_parts = name.split()
            
            # Build a list of all keywords to check against
            all_keywords = (
                location_keywords +  # ["on", "in", "at", "to", "from"]
                create_keywords +    # ["create", "make", "new"]
                delete_keywords +    # ["delete", "remove", "erase"]
                ["folder", "directory", "file"] +  # Type keywords
                ["named", "called", "with", "as", "name"] +  # Name keywords
                ["my", "the", "a", "an"] +  # Possessive words
                ["desktop", "documents", "downloads", "pictures", "music", "videos"]  # Location names
            )
            
            # Find all words that match our keywords (case-insensitive)
            for i, part in enumerate(name_parts):
                if part.lower() in all_keywords:
                    words_to_remove.append(i)
            
            # Remove the words in reverse order to maintain indices
            for i in reversed(words_to_remove):
                name_parts.pop(i)
            
            # Join the remaining words
            name = " ".join(name_parts)
            
            # Ensure the name is not empty after cleaning
            if not name:
                name = "untitled"
        
        return action, item_type, location, name

    def get_path_from_location(self, location, name):
        """Convert a location and name to a full path"""
        # Clean up the location and name
        location = location.strip().lower()
        name = name.strip()
        
        # Map common locations to their full paths
        location_map = {
            "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
            "documents": os.path.join(os.path.expanduser("~"), "Documents"),
            "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
            "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
            "music": os.path.join(os.path.expanduser("~"), "Music"),
            "videos": os.path.join(os.path.expanduser("~"), "Videos")
        }
        
        # Get the base path for the location
        if location in location_map:
            base_path = location_map[location]
        else:
            # If the location is not recognized, assume it's a full path
            base_path = location
            
            # If it's a relative path, make it absolute
            if not os.path.isabs(base_path):
                base_path = os.path.join(os.path.expanduser("~"), base_path)
        
        # Ensure the base path exists
        if not os.path.exists(base_path):
            try:
                os.makedirs(base_path, exist_ok=True)
            except Exception as e:
                print(f"Error creating directory: {str(e)}")
                # Fall back to desktop if we can't create the directory
                base_path = os.path.join(os.path.expanduser("~"), "Desktop")
        
        # Clean up the name to be a valid filename/foldername
        # Remove any invalid characters
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            name = name.replace(char, '')
            
        # Remove leading/trailing periods and spaces
        name = name.strip('. ')
        
        # If name is empty after cleaning, use a default
        if not name:
            name = "untitled"
            
        # Ensure name doesn't exceed maximum length (255 characters is a safe maximum)
        if len(name) > 255:
            name = name[:255]
        
        # Join the base path with the name and normalize it
        full_path = os.path.normpath(os.path.join(base_path, name))
        
        # Ensure we haven't escaped the base path
        if not os.path.commonpath([base_path, full_path]).startswith(base_path):
            print(f"Warning: Invalid path detected. Falling back to base path.")
            full_path = os.path.join(base_path, "untitled")
            
        return full_path

    def create_folder(self, location, name):
        """Create a folder at the specified location with the given name"""
        try:
            # Clean up the name to ensure it's a valid folder name
            name = name.strip()
            if not name:
                print("Error: Folder name cannot be empty")
                return False
                
            # Get the full path
            path = self.get_path_from_location(location, name)
            print(f"Creating folder at path: {path}")
            
            # Check if the folder already exists
            if os.path.exists(path):
                print(f"Folder already exists: {path}")
                return True
                
            # Create the folder
            self.desktop.create_folder(path)
            print(f"Successfully created folder: {path}")
            return True
        except Exception as e:
            print(f"Error creating folder: {str(e)}")
            return False

    def delete_file(self, location, name):
        """Delete a file at the specified location with the given name"""
        try:
            # Clean up the name to ensure it's a valid filename
            name = name.strip()
            if not name:
                print("Error: File name cannot be empty")
                return False
                
            # Get the full path
            path = self.get_path_from_location(location, name)
            
            # Check if the file exists before trying to delete it
            if not os.path.exists(path):
                print(f"Error: File does not exist: {path}")
                return False
                
            # Delete the file
            self.desktop.delete_file(path)
            print(f"Successfully deleted file: {path}")
            return True
        except Exception as e:
            print(f"Error deleting file: {str(e)}")
            return False

    def is_screenshot_command(self, command: str) -> bool:
        """Check if the command is a screenshot command."""
        command = command.lower()
        screenshot_keywords = ["screenshot", "capture", "take a picture", "take picture", "take photo", "save screen", "screen capture"]
        return any(keyword in command for keyword in screenshot_keywords)

    def take_screenshot(self, path: str) -> bool:
        """Take a screenshot and save it to the specified path."""
        try:
            # Ensure the screenshots directory exists
            screenshots_dir = os.path.dirname(path)
            os.makedirs(screenshots_dir, exist_ok=True)
            
            # Take the screenshot using the Desktop class
            self.desktop.capture_screen(path)
            
            # Verify the screenshot was created
            if os.path.exists(path):
                print(f"Screenshot saved to {path}")
                return True
            else:
                print(f"Failed to save screenshot to {path}")
                return False
        except Exception as e:
            print(f"Error taking screenshot: {str(e)}")
            return False

    def parse_screen_capture_command(self, command: str) -> dict:
        """Parse a screen capture command to extract the save path."""
        command = command.lower()
        # Default to saving in Pictures/Screenshots with timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        default_name = f"screenshot_{timestamp}.png"
        
        # Try to extract a custom filename
        if "as" in command or "named" in command or "called" in command:
            parts = command.split()
            try:
                idx = max(
                    parts.index("as") if "as" in parts else -1,
                    parts.index("named") if "named" in parts else -1,
                    parts.index("called") if "called" in parts else -1
                )
                if idx < len(parts) - 1:
                    name = parts[idx + 1]
                    if not name.endswith(".png"):
                        name += ".png"
                    return {"path": os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots", name)}
            except ValueError:
                pass
        
        return {"path": os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots", default_name)}

    def capture_screen(self, path: str) -> bool:
        """Capture the screen and save it to the specified path."""
        # Use the take_screenshot method to ensure consistent behavior
        return self.take_screenshot(path)

    def is_application_command(self, command: str) -> bool:
        """Check if the command is an application command."""
        command = command.lower()
        app_keywords = ["open", "close", "minimize", "maximize", "start", "launch", "run"]
        return any(keyword in command for keyword in app_keywords)

    def parse_application_command(self, command: str) -> dict:
        """Parse an application command to extract the action and app name."""
        command = command.lower()
        parts = command.split()
        
        # Find the action (open, close, minimize, maximize)
        action = None
        for keyword in ["open", "close", "minimize", "maximize", "start", "launch", "run"]:
            if keyword in parts:
                action = keyword
                break
        
        if not action:
            return None
            
        # Find the app name (everything after the action)
        try:
            app_idx = parts.index(action)
            if app_idx < len(parts) - 1:
                app_name = parts[app_idx + 1]
                return {"action": action, "app_name": app_name}
        except ValueError:
            pass
            
        return None

    def execute_command(self, command: str) -> bool:
        """Execute a voice command."""
        try:
            # Check if it's a stop command
            if command.lower() == "stop":
                self.running = False
                return True
                
            # Check if it's an application command
            if self.is_application_command(command):
                result = self.parse_application_command(command)
                if result:
                    action = result["action"]
                    app_name = result["app_name"]
                    
                    if action == "open":
                        self.open_application(app_name)
                    elif action == "close":
                        self.close_application(app_name)
                    elif action == "minimize":
                        self.minimize_application(app_name)
                    elif action == "maximize":
                        self.maximize_application(app_name)
                    return True
                    
            # Check if it's a URL command
            if self.is_url_command(command):
                result = self.parse_url_command(command)
                if result:
                    website = result["website"]
                    browser = result.get("browser")
                    self.open_url(website, browser)
                    return True
                    
            # Check if it's a file management command
            if self.is_file_management_command(command):
                result = self.parse_file_management_command(command)
                if result:
                    action = result["action"]
                    item_type = result["type"]
                    location = result["location"]
                    name = result["name"]
                    
                    if action == "create" and item_type == "folder":
                        self.create_folder(location, name)
                    elif action == "delete" and item_type == "file":
                        self.delete_file(location, name)
                    return True
                    
            # Check if it's a screenshot command
            if self.is_screenshot_command(command):
                result = self.parse_screen_capture_command(command)
                if result:
                    path = result["path"]
                    self.take_screenshot(path)
                    return True
                    
            print("I don't understand that command. Please try again.")
            return False
            
        except Exception as e:
            print(f"Error executing command: {str(e)}")
            return False

if __name__ == "__main__":
    hiccup = Hiccup()
    hiccup.run()