import random
import sqlite3

connection = sqlite3.connect("D:\\OFER\\Python\\Projects\\verbs_training\\database\\verbs.db")
cursor = connection.cursor()

def dis(verbs=[]):
    dis_index = random.randint(0, 2)
    #print(verbs)
    #print(dis_index)
    temp = verbs[dis_index]
    verbs[dis_index] = ""
    text = "INSERT INTO verbs (v1, v2, v3, miss) VALUES (\'{}\', \'{}\', \'{}\', \'{}\');".format(verbs[0], verbs[1], verbs[2], temp)
    #print(text)
    cursor.execute(text)
    connection.commit()
    #tot_list.update({verbs: temp})
    #print(verbs)
    #print(tot_list)


def start():
    cursor.execute("SELECT * FROM verbs;")
    rows = cursor.fetchall()
    #print(rows[0])
    for row in rows:
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
                            break
    while True:
        yes_no = input("Play again (type play), exit or add more verbs (type add): ")
        if yes_no.lower() == "play":
            start()
            break
        elif yes_no.lower() == "exit":
            connection.close()
            exit()
        elif yes_no.lower() == "add":
            break
        else:
            print("type play, exit or add")





while True:
    start_y_n = input("start? Y or N (type exit to exit the program): ")
    if start_y_n == "Y" or start_y_n == "y":
        start()
    elif start_y_n == "N" or start_y_n == "n":
        pass
    elif start_y_n.lower() == "exit":
        break
    elif start_y_n.lower() == "debug":
        #print(all_verbs)
        cursor.execute("SELECT * FROM verbs;")
        rows = cursor.fetchall()
        print(rows)
    elif start_y_n.lower() == "delete":
        cursor.execute("DELETE FROM verbs;")
        connection.commit()
        print("database deleted")
    v1 = input("enter v1: ")
    v2 = input("enter v2: ")
    v3 = input("enter v3: ")
    dis([v1, v2, v3])

connection.close()
