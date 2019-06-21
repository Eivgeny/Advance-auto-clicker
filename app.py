from adv_clicker import AdvClicker
from additional import tracker

z = "\n" \
    "      x             x\n" \
    "       x           x\n" \
    "           xxxxx\n" \
    "         xxxxxxxxx\n" \
    "        xx  xxx  xx\n" \
    "        xxxxxxxxxxx\n" \
    "          xxxxxxx\n"\
    "   ********GHOST*******\n"


def print_menu():
    print('\n==========================\n')
    print("r - for recording menu \n"
          "s - to start\n"
          "l - load file\n"
          "e - to exit")
    print('\n==========================\n')


print(z)
print_menu()
records: list = AdvClicker.load_file()
adv = AdvClicker()
while True:
    key = tracker()
    if key == 'r':
        adv.start_recording()
        print_menu()
    elif key == 'l':
        records = adv.load_file()
    elif key == 's':
        while True:
            if len(records) <= 0:
                print('\t\nLoad/record records before start\n')
                print_menu()
            else:
                adv.start_app(records)
            break
    elif key == 'i':
        pass
    elif key == 'e':
        break
