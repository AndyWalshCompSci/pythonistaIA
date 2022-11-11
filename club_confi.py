import datetime

club_confi = open("clubconfidence.txt", "a")

def club_conf():
    club_confi = open("clubconfidence.txt", "a")  # append mode
    while True:
        try:
            club1 = (input("Driver: (1-10) "))
            club2 = input("Woods, Hybrid and/or driving iron: (1-10) ")
            club3 = input("Irons: (1-10) ")
            club4 = input("Wedges: (1-10) ")
            club5 = input("Short game (chipping/pitching): (1-10) ")
            club6 = input("Putting (1-10) ")
        except:
            print("please give a number between 1 & 10")
        break


    #Slibers for all

    #we need a submit button at the end to save the position of the sliders
    #this function also needs to save the date this data was submitted and log in app
    #club_confi.write(club1 + " \n")
    # Append-adds at last

    #date/time module:
    ct = datetime.datetime.now()
    print("current time:-", ct)
    club_confi.write(club1 + " \n")
    club_confi.write(club2 + " \n")
    club_confi.write(club3 + " \n")
    club_confi.write(club4 + " \n")
    club_confi.write(club5 + " \n")
    club_confi.write(club6 + " \n")
    #stime stamp:
    club_confi.write(str(ct) + " \n")
    #cutting out seconds w rstrip
    ct = ''
    new_heading = ct.rstrip('.')
    print(new_heading)

club_confi.close()
