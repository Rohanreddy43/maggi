from voice import listen, speak
from brain import think
import actions, keyboard, config
import re
import logging

# Set up logging
if config.LOG_ACTIONS:
    logging.basicConfig(filename='assistant.log', level=logging.INFO, format='%(asctime)s - %(message)s')

speak(f'{config.NAME} online')

def parse_and_execute(response):
    # Simple parsing logic to identify actions in AI response
    actions_executed = []
    if 'open app' in response.lower():
        app_name = extract_param(response, 'open app')
        if app_name:
            result = actions.open_app(app_name)
            actions_executed.append(result)
            log_action(f"Opened app: {app_name}")
    if 'type text' in response.lower():
        text = extract_param(response, 'type text')
        if text:
            result = actions.type_text(text)
            actions_executed.append(result)
            log_action(f"Typed text: {text}")
    if 'press key' in response.lower():
        key = extract_param(response, 'press key')
        if key:
            result = actions.press(key)
            actions_executed.append(result)
            log_action(f"Pressed key: {key}")
    if 'click' in response.lower():
        coords = extract_coords(response)
        if coords:
            result = actions.click(coords[0], coords[1])
            actions_executed.append(result)
            log_action(f"Clicked at: {coords}")
    if 'open website' in response.lower():
        url = extract_param(response, 'open website')
        if url:
            result = actions.open_website(url)
            actions_executed.append(result)
            log_action(f"Opened website: {url}")
    if 'run command' in response.lower():
        cmd = extract_param(response, 'run command')
        if cmd:
            result = actions.run_command(cmd)
            actions_executed.append(result)
            log_action(f"Ran command: {cmd}")
    if 'create file' in response.lower():
        path = extract_param(response, 'create file')
        if path:
            result = actions.create_file(path)
            actions_executed.append(result)
            log_action(f"Created file: {path}")
    if 'delete file' in response.lower():
        path = extract_param(response, 'delete file')
        if path and (not config.CONFIRM_DESTRUCTIVE or actions.confirm_action(f"Delete file {path}?")):
            result = actions.delete_file(path)
            actions_executed.append(result)
            log_action(f"Deleted file: {path}")
    if 'browse web' in response.lower():
        url = extract_param(response, 'browse web')
        if url:
            result = actions.browse_web(url)
            actions_executed.append(result)
            log_action(f"Browsed web: {url}")
    return actions_executed

def extract_param(response, action):
    # Simple regex to extract parameter after action
    match = re.search(rf'{action}\s+(.+?)(?:\n|$)', response, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_coords(response):
    # Extract x,y coordinates
    match = re.search(r'click\s+(\d+),\s*(\d+)', response, re.IGNORECASE)
    return (int(match.group(1)), int(match.group(2))) if match else None

def log_action(action):
    if config.LOG_ACTIONS:
        logging.info(action)

while True:
    if keyboard.is_pressed('esc'):
        speak(f'{config.NAME} shutting down')
        break
    cmd = listen()
    if not cmd:
        continue
    if config.WAKE_WORD not in cmd:
        continue
    if any(w in cmd for w in config.STOP_WORDS):
        speak('Action cancelled')
        continue
    print('Command:', cmd)
    response = think(cmd)
    speak(response)
    executed_actions = parse_and_execute(response)
    if executed_actions:
        speak(f"{config.NAME}: Executed: {'; '.join(executed_actions)}")
