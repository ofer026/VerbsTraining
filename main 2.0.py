import random
import sqlite3
import time
import sys
from colorama import init, Fore, Back, Style
import os

test = {"a": "b", "c": "d"}

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
init(convert=True)
#connection = sqlite3.connect("D:\\OFER\\Python\\Projects\\verbs_training\\database\\verbs 2.0.db")
drives = ['D', 'C', 'E']
for x in drives:
    data_exists = os.path.exists("{}:\\Verb Training Game\\verbs.db".format(x))
    if data_exists:
        break
    #print(x)
if not data_exists:
    sys.stdout.write(Fore.LIGHTRED_EX + "Database not found!")
    sys.stdout.flush()
    print("\n", end='')
    print(Style.RESET_ALL, end='')
    time.sleep(0.4)
    while True:
        #global drives
        drives = ['D', 'C', 'E']
        global counter
        counter = 0
        if counter == 3:
            print(Fore.LIGHTRED_EX + "Neither drive D nor C nor E were found! \n contact developer to get a solution "
                                     "(ofer026@gmail.com")
            print(Style.RESET_ALL, end='')
            quit()
        result = os.system("mkdir \"{}:\\Verb Training Game\"".format(drives[counter]))
        if result == 1:
            if os.path.exists("{}:\\Verb Training Game".format(drives[counter])):
                break
            else:
                counter += 1
        else:
            print("Created dir named \"Verb Training Game\" in {} drive".format(drives[counter]))
            break
    time.sleep(0.2)
    connection = sqlite3.connect("{}:\\Verb Training Game\\verbs.db".format(drives[counter]))
    print("New database Created!")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE verbs ("
                   "v1 TEXT,"
                   "v2 TEXT,"
                   "v3 TEXT);")
    connection.commit()
elif data_exists:
    while True:
        drives = ['D', 'C', 'E']
        counter = 0
        try:
            connection = sqlite3.connect("{}:\\Verb Training Game\\verbs.db".format(drives[counter]))
        except sqlite3.OperationalError:
            counter += 1
        else:
            break
    cursor = connection.cursor()
#print(path)

#print(Fore.RED + "test")
sleep_time = 0.041
def welcome():
    welcome_message = "========== Welcome to english verb training game! =========="
    text = "============================================================"
    credits = "===== Creator: Ofer Ovadia. Email: ofer026@gmail.com  ======"
    for x in range(0, len(text)):
        sys.stdout.write(Fore.LIGHTGREEN_EX + text[x])
        sys.stdout.flush()
        time.sleep(sleep_time)
    sys.stdout.write("\n")
    sys.stdout.flush()
    for x in range(0, len(text)):
        sys.stdout.write(Fore.LIGHTMAGENTA_EX + text[x])
        time.sleep(sleep_time)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
    for x in range(0, len(text)):
        sys.stdout.write(Fore.LIGHTCYAN_EX + welcome_message[x])
        time.sleep(sleep_time)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
    for x in range(0, len(text)):
        color_text = Fore.RED + credits[x]
        print(Fore.LIGHTRED_EX + credits[x], end='')
        time.sleep(sleep_time)
        #sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
    for x in range(0, len(text)):
        sys.stdout.write(Fore.LIGHTYELLOW_EX + text[x])
        time.sleep(sleep_time)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
    for x in range(0, len(text)):
        sys.stdout.write(Fore.LIGHTBLUE_EX + text[x])
        time.sleep(sleep_time)
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
    print(Style.RESET_ALL, end='')
    # print("====================================================")
    # print("====================================================")
    # print("====== Welcome to english verb training game! ======")
    # print("====================================================")
    # print("====================================================")
def add(verbs=[]):
    #dis_index = random.randint(0, 2)
    #print(verbs)
    #print(dis_index)
    #temp = verbs[dis_index]
    #verbs[dis_index] = ""
    text = "INSERT INTO verbs (v1, v2, v3) VALUES (\'{}\', \'{}\', \'{}\');".format(verbs[0], verbs[1], verbs[2])
    cursor.execute(text)
    connection.commit()
    #print(verbs)


'''    for row in rows:
        for verb in row:
            if row[row.index(verb)] == "":
                #print("verb is {}".format(verb))
                while True:
                    in_verb = input("{} what is the missing verb? ".format(row[0:3]))
                    if in_verb.lower() == row[3].lower():
                        print("Correct!")
                        break
                    else:
                        ans = input("Wrong! type skip to continue or leave blank to keep trying: ")
                        if ans.lower() == "skip":
                            break'''
def start():
    cursor.execute("SELECT * FROM verbs;")
    rows = cursor.fetchall()
    #print(rows[0])

    for row in rows:
        #print(row)
        row = list(row)
        dis_index = random.randint(0, 2)
        miss = row[dis_index]
        row[dis_index] = ""
        row.append(miss)
        while True:
            in_verb = input("{} what is the missing verb? ".format(row[0:3]))
            if in_verb.lower() == row[3].lower():
                print("Correct!")
                break
            else:
                ans = input("Wrong! type skip to continue or leave blank to keep trying: ")
                if ans.lower() == "skip":
                    break
    while True:
        yes_no = input("Play again (type play), exit or add more verbs (type add): ")
        if yes_no.lower() == "play":
            start()
            break
        elif yes_no.lower() == "exit":
            connection.close()
            quit()
        elif yes_no.lower() == "add":
            break
        else:
            print("type play, exit or add")

welcome()
time.sleep(0.5)

while True:
    start_y_n = input("Do you want to start playing? (type play or \'y\') \nDo you want to delete the database and start? "
                      "again (type delete) \nIf you want to want to what is in the database type show \nIf you want "
                      "to add more verbs type either n or add or leave blank \nIf "
                      "you want to exit type exit \nYour choice: ")
    if start_y_n == "Y" or start_y_n == "y" or start_y_n.lower() == "play":
        start()
    elif start_y_n == "N" or start_y_n == "n" or start_y_n.lower() == "add":
        pass
    elif start_y_n.lower() == "exit":
        break
    elif start_y_n.lower() == "debug" or start_y_n.lower() == "show":
        #print(all_verbs)
        cursor.execute("SELECT * FROM verbs;")
        rows = cursor.fetchall()
        #print("Found!")
        print(rows)
    elif start_y_n.lower() == "delete":
        cursor.execute("DELETE FROM verbs;")
        connection.commit()
        print("database deleted")
    v1 = input("enter v1: ")
    v2 = input("enter v2: ")
    v3 = input("enter v3: ")
    add([v1, v2, v3])

connection.close()

# TODO Check what to do when you don't always see the color (text) in some places and instead there is some weird staff (done - (colorama.)init() was misplaced
# TODO add an option to create the database in C: drive (done, also avaliable to put the database on E drive (if non of the three drives are found, the program prints an error message and saying to contact developer at gmail and then quits the program)
# TODO try to find every error (done, 1 possible error found - a database not found (in x drive) and than he moves to the next drive (drives - D, C, E). need to know if somehow it can still make an error)
# TODO give the file (at least the .exe) a new name (given - Verb Training Game)
# TODO find a fitting icon (found)
# TODO correct the error of 'no such table: verbs' (look at log.txt)
# TODO make to .exe again after all above is done
