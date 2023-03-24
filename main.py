import pywhatkit, pyautogui, time, schedule, os

os.system("cls")
print("Make sure you logged in whatsapp web on your default browser.")
input("Press any key to continue...")

number = "+90555xxxxxxx" #Make sure you added country code
message = "Your Message"

def send_message():
    pywhatkit.sendwhatmsg_instantly(number, message, 10, tab_close=True)
    time.sleep(5)
    pyautogui.press('enter')


schedule.every().day.at("05:40").do(send_message) ## change the 05:40 value

while True:
    schedule.run_pending()
    time.sleep(1)