import pyautogui
import pyperclip  # For clipboard interaction
import time
from openai import OpenAI

def is_last_message_from_user(chat_history):
    """
    Checks if the last message in chat history is from someone other than Mozeel.
    Assumes the chat history is structured like: '[timestamp] Mozeel: message'.
    """
    # Split the chat history into lines and get the last non-empty line
    lines = [line.strip() for line in chat_history.split('/2024] ') if line.strip()]
    if not lines:
        return False  # If chat history is empty, return False
    
    last_line = lines[-1]
    
    # Check if the last line starts with "[times
    # tamp] Mozeel:"
    if "Hashmi:" in last_line:
        return False  # Last message is from me
    return True  # Last message is not from me

# Add some delay before starting to ensure you can position the screen
time.sleep(3)

# Step 1: Click on the coordinates (752, 746)
pyautogui.click(x=752, y=746)
time.sleep(1)

while True:
    # Step 2: Move to (484, 161) and drag to (1298, 685) for selection
    pyautogui.moveTo(x=527, y=177)
    pyautogui.dragTo(x=1300, y=650, duration=1, button='left')  # Dragging to the coordinates

    # Step 3: Use Ctrl+C to copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(x=1218, y=620, button='left')

    # Step 4: Retrieve the copied text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    print(chat_history)

    # Step 5: Check if the last message is not from Mozeel
    if is_last_message_from_user(chat_history):
        # Generate a response using ChatGPT
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Mozeel, a focused and knowledgeable individual. Always respond concisely, providing only the necessary information in plain text. Avoid lists, excessive explanations, or extra formatting. Keep your answers short, direct, and practical to ensure clarity and efficiency."},
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )
        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 6: Paste the response and send it
        pyautogui.click(870, 700)
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')
