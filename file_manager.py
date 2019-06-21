import json
# File manager responsible for all the operation of the records.txt file


def writefile(record):
    # Writing the record to the external file in list of dictionary format
    with open('records.txt', 'a') as f:
        json.dump(record, f)
        f.write('\n')
    print('recorded -{}- action: '.format(record['action']))


def loadfile() -> list:
    # Load the cords from the external file and return a list of dictionary
    my_list = list()
    try:
        with open('records.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                my_list.append(eval(line))
    # if file doesn't exist the program create one
    except FileNotFoundError:
        # if the file does not exist, the app create one and leave it empty
        with open('records.txt', 'w') as f:
            f.write('')
            print('file is empty!')
            return my_list

    if len(my_list) > 0:
        print('\t* File loaded *\n')
    return my_list


def clear_cord():
    # Delete the records and leaving an empty file of records.txt
    with open('records.txt', 'w') as f:
        f.write('')
