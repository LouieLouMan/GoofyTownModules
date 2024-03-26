import ctypes

BOOLY0 = False
BOOLY1 = False
BOOLY2 = False
BOOLY3 = False
BOOLY4 = False
COUNTER = 0

def add(x: int, y: int):
    return CONDITIONS.get((BOOLY0, BOOLY1, BOOLY2, BOOLY3, BOOLY4))(x, y)

def normal(x, y):
    global COUNTER
    global BOOLY4
    if COUNTER >= 5:
        BOOLY4 = True
        COUNTER = 0
    else:
        COUNTER += 1
    return x + y

def windows_alert_adding(x, y):
    global BOOLY3
    global BOOLY4
    BOOLY4 = False
    BOOLY3 = True

    WS_EX_TOPMOST = 0x40000
    window_title = "ALERT"
    message = "I am adding up..."

    ctypes.windll.user32.MessageBoxExW(None, message, window_title, WS_EX_TOPMOST)

    return x + y

def normal_string(x, y):
    global BOOLY4
    BOOLY4 = True
    return str(x + y)



    
CONDITIONS = {
    (True, True, True, True, True): lambda: print("All conditions are True"),
    (True, True, True, True, True): lambda: print("All conditions are True"),
    (True, True, True, True, False): lambda: print("All conditions are True"),
    (True, True, True, False, True): lambda: print("All conditions are True"),
    (True, True, True, False, False): lambda: print("All conditions are True"),
    (True, True, False, True, True): lambda: print("All conditions are True"),
    (True, True, False, True, False): lambda: print("All conditions are True"),
    (True, True, False, False, True): lambda: print("All conditions are True"),
    (True, True, False, False, False): lambda: print("All conditions are True"),
    (True, False, True, True, True): lambda: print("All conditions are True"),
    (True, False, True, True, False): lambda: print("All conditions are True"),
    (True, False, True, False, True): lambda: print("All conditions are True"),
    (True, False, True, False, False): lambda: print("All conditions are True"),
    (True, False, False, True, True): lambda: print("All conditions are True"),
    (True, False, False, True, False): lambda: print("All conditions are True"),
    (True, False, False, False, True): lambda: print("All conditions are True"),
    (True, False, False, False, False): lambda: print("All conditions are True"),
    (False, True, True, True, True): lambda: print("All conditions are True"),
    (False, True, True, True, False): lambda: print("All conditions are True"),
    (False, True, True, False, True): lambda: print("All conditions are True"),
    (False, True, True, False, False): lambda: print("All conditions are True"),
    (False, True, False, True, True): lambda: print("All conditions are True"),
    (False, True, False, True, False): lambda: print("All conditions are True"),
    (False, True, False, False, True): lambda: print("All conditions are True"),
    (False, True, False, False, False): lambda: print("All conditions are True"),
    (False, False, True, True, True): lambda: print("All conditions are True"),
    (False, False, True, True, False): lambda: print("All conditions are True"),
    (False, False, True, False, True): lambda: print("All conditions are True"),
    (False, False, True, False, False): lambda: print("All conditions are True"),
    (False, False, False, True, True): lambda: print("All conditions are True"),
    (False, False, False, True, False): normal_string,
    (False, False, False, False, True): windows_alert_adding,
    (False, False, False, False, False): normal,
}

    
if __name__ == "__main__":
    for i in range(8):
        num = add(1,2)
        print(type(num), num)