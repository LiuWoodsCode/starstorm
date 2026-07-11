# As I'm working on a MacBook Neo and this code assumes Windows, 
# I need some stubs to make sure the code even works

# Common constants
HKEY_CLASSES_ROOT = object()
HKEY_CURRENT_USER = object()
HKEY_LOCAL_MACHINE = object()
HKEY_USERS = object()
HKEY_CURRENT_CONFIG = object()

REG_SZ = 1
REG_DWORD = 4
REG_QWORD = 11

KEY_READ = 0x20019
KEY_WRITE = 0x20006
KEY_ALL_ACCESS = 0xF003F


class RegistryKey:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"<RegistryKey {self.path!r}>"


def OpenKey(root, sub_key, reserved=0, access=KEY_READ):
    return RegistryKey(sub_key)


def CreateKey(root, sub_key):
    return RegistryKey(sub_key)


def CloseKey(key):
    pass


def QueryValueEx(key, value_name):
    raise FileNotFoundError("Registry value not found")


def SetValueEx(key, value_name, reserved, reg_type, value):
    pass


def DeleteValue(key, value_name):
    pass


def DeleteKey(root, sub_key):
    pass


def EnumKey(key, index):
    raise OSError("No more data")


def EnumValue(key, index):
    raise OSError("No more data")


def QueryInfoKey(key):
    return (0, 0, 0)


def ConnectRegistry(computer_name, key):
    return key


def FlushKey(key):
    pass


def LoadKey(root, sub_key, file_name):
    raise NotImplementedError


def SaveKey(key, file_name):
    raise NotImplementedError


def ExpandEnvironmentStrings(value):
    import os
    return os.path.expandvars(value)