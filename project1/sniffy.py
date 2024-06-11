import keyboard
import sys

def on_key_press(event):
    if event.name == "space":
        print("Space was pressed")
        return False  # Stop the event handler
    elif event.name == "escape":
        print("Escape was pressed, exiting program")
        sys.exit()
           
keyboard.on_press(on_key_press)

while True:

    print("Press 'space' to trigger the event...")
    keyboard.read_event()



print("Program finished") 