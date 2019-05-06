import _winreg

KEY = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU'

kk = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, KEY, 0, _winreg.KEY_ALL_ACCESS)


def print_history():
    for i in xrange(0, _winreg.QueryInfoKey(kk)[1]):
        his = _winreg.EnumValue(kk, i)
        if not his[0] == 'MRUList':
            print his[1]


def delhistory():
    arr = []
    for i in xrange(0, _winreg.QueryInfoKey(kk)[1]):
        his = _winreg.EnumValue(kk, i)
        if not his[0] == 'MRUList':
            arr.append(his)
    delit = raw_input('enter the name of the one you wanna delete--> ')
    for j in arr:
        if str(j[0]) == delit:
            _winreg.DeleteKey(kk, delit)
            print 'deleted'
        else:
            print 'not found'

print_history()
delhistory()
print_history()