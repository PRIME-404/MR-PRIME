import platform
b = platform.architecture()[0]
if b == '64bit':
    import PRIME
elif b == '32bit':
    print("Sorry 32bit Not Supported!")
