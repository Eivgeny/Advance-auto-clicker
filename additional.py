import msvcrt


def tracker() -> str:
    # waiting to key to press and return the key wia str

    while True:
        if msvcrt.kbhit():
            key = (str(msvcrt.getch())[2:-1])
            break
    return key
