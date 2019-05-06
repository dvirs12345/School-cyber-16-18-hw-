import win32gui
import ctypes

def mb():
    if win32gui.MessageBox(None, "Its an Error", "Error", 0x00000030L | 0x00000004L | 0x00004000L) == 6:
        print 'yes'
    else:
        print 'no'


# win32ui.MessageBox("Its an Error", "Error", 0x00000030L | 0x00000004L | 0x00004000L)
def wuteven():
    my_library = ctypes.WinDLL("User32.dll")
    my_library.MessageBoxA(None, "Its an Error", "Error", 0x00000030L | 0x00000004L | 0x00004000L)

mb()
wuteven()