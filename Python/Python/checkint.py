def checkInt(a,b):
    try:
        int(a) and int(b)
        return True
    except:
        ValueError
        return False


print(checkInt(False,10))