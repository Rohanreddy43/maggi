import pyautogui, subprocess, os, webbrowser, shutil, requests
from bs4 import BeautifulSoup
import keyboard
pyautogui.FAILSAFE = True

def open_app(a):
    try:
        subprocess.Popen(a, shell=True)
        return "App opened successfully."
    except Exception as e:
        return f"Failed to open app: {str(e)}"

def type_text(t):
    pyautogui.write(t, interval=0.02)
    return "Text typed."

def press(k):
    pyautogui.press(k)
    return "Key pressed."

def click(x, y):
    pyautogui.click(x, y)
    return "Clicked at position."

def open_website(u):
    webbrowser.open(u)
    return "Website opened."

def run_command(c):
    try:
        result = os.system(c)
        return f"Command executed with result: {result}"
    except Exception as e:
        return f"Failed to run command: {str(e)}"

def create_file(path, content=""):
    try:
        with open(path, 'w') as f:
            f.write(content)
        return f"File created: {path}"
    except Exception as e:
        return f"Failed to create file: {str(e)}"

def edit_file(path, old_content, new_content):
    try:
        with open(path, 'r') as f:
            data = f.read()
        data = data.replace(old_content, new_content)
        with open(path, 'w') as f:
            f.write(data)
        return f"File edited: {path}"
    except Exception as e:
        return f"Failed to edit file: {str(e)}"

def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
        return f"File deleted: {path}"
    else:
        return "File not found."

def move_file(src, dst):
    try:
        shutil.move(src, dst)
        return f"File moved from {src} to {dst}"
    except Exception as e:
        return f"Failed to move file: {str(e)}"

def browse_web(url, extract_info=False):
    try:
        response = requests.get(url)
        if extract_info:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title"
            return f"Page title: {title}"
        return "Web page accessed."
    except Exception as e:
        return f"Failed to browse web: {str(e)}"

def confirm_action(action_desc):
    # For now, ask via voice input; in future, could use GUI or other methods
    from voice import speak, listen
    speak(f"Are you sure you want to {action_desc}? Say yes or no.")
    response = listen()
    return 'yes' in response.lower() if response else False
