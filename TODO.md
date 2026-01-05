# TODO: Enhance AI Assistant to Match Advanced Prompt

## Step 1: Update System Prompt in brain.py
- [x] Replace the simple system prompt with the detailed prompt from feedback for better AI behavior and capabilities.

## Step 2: Expand actions.py with Additional Functions
- [x] Add functions for file operations (create, edit, delete, move files/folders).
- [x] Add functions for web browsing and information extraction.
- [x] Add functions for running scripts/commands with safety checks.
- [x] Add functions for system settings control (if possible).

## Step 3: Modify main.py to Parse and Execute Actions
- [x] After receiving response from think(), parse the response to identify actions (e.g., keywords like "open app", "type text").
- [x] Execute corresponding functions from actions.py.
- [x] Add logic for multi-step tasks and autonomy.

## Step 4: Implement Safety and Confirmation Mechanisms
- [x] Add confirmation prompts for destructive actions (e.g., delete files).
- [x] Handle stop words and cancellations properly.
- [x] Add error handling and logging.

## Step 5: Enhance Voice and Interaction
- [x] Improve voice recognition reliability (add retries or fallbacks).
- [x] Ensure natural language handling as per prompt.

## Step 6: Test and Refine
- Run tests for key functionalities (voice input, action execution).
- Verify safety features and error handling.
