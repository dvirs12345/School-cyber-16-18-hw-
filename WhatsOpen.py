# Dvir Sadon
import win32gui


def enumhandler(hwnd, shit):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        print title


win32gui.EnumWindows(enumhandler, 0)
