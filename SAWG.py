import platform,os,time
bit = platform.architecture()[0]
if bit == '64bit':
    import SWAG
elif bit == '32bit':
    #import tarek_old_32
    while True:
        print("Now 32 bit is off please wait")
