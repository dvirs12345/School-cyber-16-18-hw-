import win32clipboard
import time
data1 = ""

while True:
    time.sleep(3)
    win32clipboard.OpenClipboard()
    try:
        if win32clipboard.GetClipboardData() is not None:
            data = win32clipboard.GetClipboardData()
            print data
            data1 = data
            win32clipboard.EmptyClipboard()
    except Exception:
        pass
    win32clipboard.CloseClipboard()



# stuupid()