import ctypes
import random
import time
import os
import sys
import traceback

BOOLY0 = False
BOOLY1 = False
BOOLY2 = False
BOOLY3 = False
BOOLY4 = False
COUNTER = 0

def add(x: int, y: int):
    if (x == 9 and y == 10) or (x == 10 and y == 9):
        return 21
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

def __windows_alert_adding(x, y):
    global BOOLY3
    global BOOLY4
    BOOLY4 = False
    BOOLY3 = True

    WS_EX_TOPMOST = 0x40000
    window_title = "ALERT"
    message = "I am adding up..."

    ctypes.windll.user32.MessageBoxExW(None, message, window_title, WS_EX_TOPMOST)

    return x + y

def __normal_string(x, y):
    global BOOLY4
    BOOLY4 = True
    return str(x + y)

def __i_dont_know(x, y):
    global BOOLY0
    global BOOLY1
    global BOOLY2
    global BOOLY3
    global BOOLY4
    BOOLY2 = True
    BOOLY3 = False
    BOOLY4 = False

    print(f"Is {x} + {y} = {x + y + 1}?")
    if answer := input("Is it? "):
        if answer == "yes":
            BOOLY0 = BOOLY1 = BOOLY2 = BOOLY3 = BOOLY4 = True
            return x + y + 1
        print("Oh...")
        return "Sorry..."
    print("Okay or just don't answer me")
    return x + y

def __error(x, y):
    global BOOLY0
    global BOOLY1
    global BOOLY2
    global BOOLY3
    global BOOLY4
    BOOLY0 = True if random.randint(0, 1) else False
    BOOLY1 = True if random.randint(0, 1) else False
    BOOLY2 = True if random.randint(0, 1) else False
    BOOLY3 = True if random.randint(0, 1) else False
    BOOLY4 = True if random.randint(0, 1) else False

    __adder_helper()

    time.sleep(5)
    return x + y

def __return_user(x, y):
    return os.getlogin()

def __runner(x, y):
    for _ in range(1000000 + x):
        for _ in range(1000 + y):
            pass

    return x + y

def __conways_game_of_life(x, y):
    global BOOLY0
    global BOOLY1
    global BOOLY2
    global BOOLY3
    global BOOLY4
    BOOLY0 = BOOLY1 = BOOLY2 = BOOLY3 = BOOLY4 = False
    __run_game(x, y)
    return {f"{x + y}": x+y}


def __clear_console():
    """
    Clears the console using a system command based on the user's operating system.

    """

    if sys.platform.startswith('win'):
        os.system("cls")
    elif sys.platform.startswith('linux'):
        os.system("clear")
    elif sys.platform.startswith('darwin'):
        os.system("clear")
    else:
        print("Unable to clear terminal. Your operating system is not supported.\n\r")


def __resize_console(rows, cols):
    if cols < 32:
        cols = 32

    if sys.platform.startswith('win'):
        command = "mode con: cols={0} lines={1}".format(cols + cols, rows + 5)
        os.system(command)
    elif sys.platform.startswith('linux'):
        command = "\x1b[8;{rows};{cols}t".format(rows=rows + 3, cols=cols + cols)
        sys.stdout.write(command)
    elif sys.platform.startswith('darwin'):
        command = "\x1b[8;{rows};{cols}t".format(rows=rows + 3, cols=cols + cols)
        sys.stdout.write(command)
    else:
        print("Unable to resize terminal. Your operating system is not supported.\n\r")


def __create_initial_grid(rows, cols):
    grid = []
    for _ in range(rows):
        grid_rows = []
        for _ in range(cols):
            if random.randint(0, 7) == 0:
                grid_rows += [1]
            else:
                grid_rows += [0]
        grid += [grid_rows]
    return grid


def __print_grid(rows, cols, grid, generation):
    __clear_console()
    output_str = ""
    output_str += "Generation {0} - To exit the program press <Ctrl-C>\n\r".format(generation)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                output_str += ". "
            else:
                output_str += "@ "
        output_str += "\n\r"
    print(output_str, end=" ")


def __create_next_grid(rows, cols, grid, next_grid):
    for row in range(rows):
        for col in range(cols):
            live_neighbors = __get_live_neighbors(row, col, rows, cols, grid)
            if live_neighbors < 2 or live_neighbors > 3:
                next_grid[row][col] = 0
            elif live_neighbors == 3 and grid[row][col] == 0:
                next_grid[row][col] = 1
            else:
                next_grid[row][col] = grid[row][col]


def __get_live_neighbors(row, col, rows, cols, grid):
    life_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                life_sum += grid[((row + i) % rows)][((col + j) % cols)]
    return life_sum


def __grid_changing(rows, cols, grid, next_grid):
    for row in range(rows):
        for col in range(cols):
            if not grid[row][col] == next_grid[row][col]:
                return True
    return False


def __get_integer_value(prompt, low, high):
    while True:
        try:
            value = int(prompt)
        except ValueError:
            print("Input was not a valid integer value.")
            continue
        if value < low or value > high:
            value = high
            break
        else:
            break
    return value


def __run_game(x, y):
    __clear_console()
    rows = __get_integer_value(x*32, 10, 60)
    __clear_console()
    cols = __get_integer_value(y*12, 10, 118)

    generations = 30
    __resize_console(rows, cols)

    current_generation = __create_initial_grid(rows, cols)
    next_generation = __create_initial_grid(rows, cols)

    gen = 1
    for gen in range(1, generations + 1):
        if not __grid_changing(rows, cols, current_generation, next_generation):
            break
        __print_grid(rows, cols, current_generation, gen)
        __create_next_grid(rows, cols, current_generation, next_generation)
        time.sleep(1 / 5.0)
        current_generation, next_generation = next_generation, current_generation

    __print_grid(rows, cols, current_generation, gen)

def __adder_helper():
    __optimizer()

def __optimizer():
    __get_filepath()

def __get_filepath():
    __add_x_to_y()

def __add_x_to_y():
    __calculate_x_to_precision_float()

def __calculate_x_to_precision_float():
    __calculate_y_to_precision_float()

def __calculate_y_to_precision_float():
    __delegate_to_c()

def __delegate_to_c():
    __validate_numbers()

def __validate_numbers():
    __create_numbers()

def __create_numbers():
    try: 
        print(ValueError.with_traceback())
    except Exception as e:
        try: 
            print(e.with_traceback(e))
        except Exception as e:
            traceback.print_stack()
    return


CONDITIONS = {
    (True, True, True, True, True): __conways_game_of_life,
    (True, True, True, True, False): normal,
    (True, True, True, False, True): normal,
    (True, True, True, False, False): normal,
    (True, True, False, True, True): normal,
    (True, True, False, True, False): normal,
    (True, True, False, False, True): normal,
    (True, True, False, False, False): normal,
    (True, False, True, True, True): normal,
    (True, False, True, True, False): normal,
    (True, False, True, False, True): normal,
    (True, False, True, False, False): normal,
    (True, False, False, True, True): normal,
    (True, False, False, True, False): normal,
    (True, False, False, False, True): normal,
    (True, False, False, False, False): normal,
    (False, True, True, True, True): normal,
    (False, True, True, True, False): normal,
    (False, True, True, False, True): normal,
    (False, True, True, False, False): normal,
    (False, True, False, True, True): normal,
    (False, True, False, True, False): normal,
    (False, True, False, False, True): normal,
    (False, True, False, False, False): normal,
    (False, False, True, True, True): normal,
    (False, False, True, True, False): __runner,
    (False, False, True, False, True): __return_user,
    (False, False, True, False, False): __error,
    (False, False, False, True, True): __i_dont_know,
    (False, False, False, True, False): __normal_string,
    (False, False, False, False, True): __windows_alert_adding,
    (False, False, False, False, False): normal,
}

    
if __name__ == "__main__":
    print("hi")
    for i in range(100):
        num = add(i,2)
        print(type(num), num)
        print()
    print(__runner(1, 2))
