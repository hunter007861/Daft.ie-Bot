import pyautogui as pt
from time import sleep
import pyperclip

sleep(3)


def get_mail():
    global x, y
    pt.moveTo(846, 865, duration=.05)

    for i in range(100):
        nextButton = pt.locateOnScreen("bot/nextButton.png", confidence=.9)
        if nextButton is not None:
            pt.alert("change the page")
            sleep(10)
            pt.moveTo(846, 865, duration=.05)
            pt.scroll(-300)
            continue
        pt.click()
        sleep(2)
        pt.scroll(-500)
        position2 = pt.locateOnScreen("bot/email.png", confidence=.9)
        if position2 is None:
            pt.alert("cannot find email go back")
            sleep(10)
            pt.moveTo(846, 865, duration=.05)
            pt.scroll(-300)
            continue
        x = position2[0]
        y = position2[1]
        pt.moveTo(x + 20, y + 20, duration=.05)
        pt.click()
        sleep(1)
        position3 = pt.locateOnScreen("bot/nameTag.png", confidence=.6)
        if position3 is not None:
            x = position3[0]
            y = position3[1]
            pt.moveTo(x+20, y+50, duration=.05)
            pt.click()
            pt.write("Sarvesh Bhosale")
            pt.moveTo(x + 20, y + 180, duration=.05)
            pt.click()
            pt.write("sarveshbhosale111@gmail.com")
            pt.moveTo(x + 20, y + 310, duration=.05)
            pt.click()
            pt.write("+353899756487")
            pt.moveTo(x + 20, y + 440, duration=.05)
            pt.click()
            pt.typewrite("Hello, hope you are having a good day me and my 2 friends are searching for a appartment and this suits my needs, We are financially stable & financially secured so your pay wont be the problem. We are very sincere, well behaved, clean and not party animals. We belong to a very cultured and disciplined families. We are planning to  let the apartment for 12 months & more. Can you please arrange a viewing for us to inspect the property. Looking forward to hearing from you soon. Thanks a lot. We are available for immediate so we have finance ready too. Thanks regards Sarvesh Bhosale")
            sleep(0.5)
            pt.moveTo(x + 20, y + 400, duration=.05)
            pt.click()
            pt.scroll(-100)
            sleep(1)
            send = pt.locateOnScreen("bot/send.png")
            x = send[0]
            y = send[1]
            pt.moveTo(x, y, duration=.05)
            pt.click()
            sleep(2)
            close = pt.locateOnScreen("bot/close.png")
            if close is None:
                pt.alert("already sent go back")
                sleep(10)
                pt.moveTo(846, 865, duration=.05)
                pt.scroll(-300)
                continue
            x = close[0]
            y = close[1]
            pt.moveTo(x+10, y+10, duration=.05)
            pt.click()
            backbutton = pt.locateOnScreen("bot/backbutton.png")
            x = backbutton[0]
            y = backbutton[1]
            pt.moveTo(x, y, duration=.05)
            pt.click()
            sleep(1)
        else:
            pt.alert("cannot find name go back")
            sleep(10)
            pt.moveTo(846, 865, duration=.05)
            pt.scroll(-300)
            continue
        pt.moveTo(846, 865, duration=.05)
        pt.scroll(-300)
        sleep(2)


get_mail()
