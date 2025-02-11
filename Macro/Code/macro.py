import json
import keyboard
import pyautogui
import time

def waitSpace():
    while True:
        if keyboard.is_pressed('space'):
            break

#stores positions into json file
def definePositions():
    #sets positions for gotit, answer, and close buttons
    def setpos(item):
        time.sleep(.1)
        print("Press space to set position of " + item + ".")
        waitSpace()
        return pyautogui.position()

    positions = {
        "gotit" : [0, 0],
        "answer" : [0, 0],
        "close" : [0, 0],
    }

    positions["gotit"] = setpos("gotit (after awnsering incorectly)")
    positions["answer"] = setpos("answer (first or second box)")
    positions["close"] = setpos("close (X in the incomplete awnsers box)")

    #writes positions to json file
    with open('positions.json', 'w', encoding='utf-8') as f:
        json.dump(positions, f, indent=4, ensure_ascii=False)

    time.sleep(.1)
    print("Positions saved to positions.json")

def runMacro():
    #loads JSON file
    with open('positions.json', 'r') as f:
        pos = json.load(f)

    #function to click through the page
    def clickthrough():
        pyautogui.click(pos["gotit"][0], pos["gotit"][1])

        pyautogui.moveTo(pos["answer"][0], pos["answer"][1])
        pyautogui.mouseDown()
        time.sleep(.1)
        pyautogui.mouseUp()

        pyautogui.press("enter")

        pyautogui.click(pos["close"][0], pos["close"][1])

    run = True
    while run:

        clickthrough()

        #waits for user to press p to stop the macro
        if keyboard.read_key() == 'p':
            run = False

    print("stoped")

def main():

    print("")
    print("IXL macro by anonymous.")
    print("Use at your own risk.")
    print("")

    while True:
        print("1. Define positions")
        print("2. Run macro")
        print("3. instructions")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            definePositions()
        elif choice == '2':
            runMacro()
        elif choice == '3':
            print("""
                Instructions:
               
                If this is first time running the program,
                select option 3 to read the instructions.
                Then select option 1 to define the positions of
                the buttons.
                  
                Select option 2 to run the macro. Run a 50/50
                skill, ex, AQ2. Press & hold control to make it
                work. Press P to stop it.
               
                You do not need to read the instructions,
                or redefine the positions if you have already
                done so.

                  
                Warnings:
                 
                Skills that are complete will not result in
                increased placement. The creator nor distributor
                of this program is not liable for the harm it may
                cause if misused. Use at your own risk. You are
                free to share this program, but do not claim it as your
                own.
                """)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

main()