from pyautogui import position, pixel
from file_manager import clear_cord, writefile
from additional import tracker
# recorder responsible to manage the recording proses


def rec(option):
    color_position = position()  # store the pixel coordinates
    color = pixel(color_position[0], color_position[1])  # use the coordinates to get RGB color code
    while True:
        key = tracker()
        if key == 'f':
            click_position = position()  # get the coordinates of the needed mouse click
            # store the color with the coordinates and the mouse click coordinates to a dictionary
            record = {'action': option,
                      'click': (click_position[0], click_position[1]),
                      'color': color,
                      'check': (color_position[0], color_position[1])}
            # send the created dictionary to file_manager
            writefile(record)
            break
        if key == 'n':
            print('Cancel movement')
            break
    else:
        pass


def start_recording():
    # print out recording menu
    print('\n==========================\n')
    print('** Start recording **\n')
    print("m - for rec movement \n"
          "c - for rec cutting \n"
          "i - for rec cutting \n"
          "\tf - for confirm record\n"
          "\tn - to cancel\n"
          "r - reset records\n"
          "e - exit")
    print('\n==========================\n')
    while True:
        key = tracker()
        if key == 'm':
            rec('move')
        if key == 'c':
            rec('cut')
        if key == 'r':
            print('RESET RECORDS!')
            clear_cord()
        if key == 'i':
            pass
        if key == 'e':
            print('** exit from rec mode! **\n')
            break
    else:
        pass
