from peewee import *
from collections import OrderedDict
import sys
from random import randint

db = SqliteDatabase('Passenger_3rdtry.db')

class Passenger1(Model):

    passenger = CharField(max_length=255, unique=True)
    program = CharField(max_length=255)
    program2 = CharField(max_length=255)

    class Meta:
        database = db
def initialize():
    db.connect()
    db.create_tables([Passenger1])

def join_program(passeng) :
    # program_choice = input("Select a frequent flyer travel program to join: \n1.Delta\n2.American")
    """join program(s)"""
    print("Select a frequent flyer travel program to join: \n1.Delta\n2.American"
          "\nPress control-D when finished")
    data = sys.stdin.read().strip()  # read all of the data that comes in
    # data = input("Enter traveler name: ")
    null = True
    if data:
        add_another_program = input("do you want to add another program? y/n")
        if add_another_program == "n":
            try:
                inp = input("save entry y or n ").lower()
                if inp != "n":
                    Passenger1.create(passenger=passeng,program=data,program2=null)
                    print("prgram saved succesfully")
            except IntegrityError:
                print("hit integ error")
                pass
        added_new_passenger(passeng,data,None)
        if add_another_program == "y":
            print("Select a frequent flyer travel program to join: \n1.Delta\n2.American"
                  "\nPress control-D when finished")
            data2 = sys.stdin.read().strip()  # read all of the data that comes in
            if data2:
                try:
                    inp = input("save entry y or n ").lower()
                    if inp != "n":
                        Passenger1.create(passenger=passeng, program=data, program2=data2)
                        print("Program 2 saved succesfully")
                except IntegrityError:
                    print("hit integ error")
                    pass
            added_new_passenger(passeng,data,data2)
def added_new_passenger(passeng,data,data2):
    if data == "1":
        data = "Delta Airlines Frequent Flier Program"
    if data == "2":
        data = "American Airlines Frequent Flier Program"
    if data2 == "1":
        data2 = "Delta Airlines Frequent Flier Program"
    if data2 == "2":
        data2 = "American Airlines Frequent Flier Program"
    print("Added new traveler")
    print("Name: {}".format(passeng))
    student = Passenger1.select().order_by(Passenger1.id.desc()).get() #sort Passenger1.id's in desc order, get the first one
    print("Memberships: \n{}\nMembership Number = {}\n{}\nMembership Number = {}".format(data,student,data2,student))
    # id_num = Passenger1.select()
    # for id_nums in id_num:
    #     print("ID NUMBER")
    #     print(id_nums.id)
    # student2 = Passenger1.select().order_by(Passenger1.passenger.get()) #sort Passenger1.id's in desc order, get the first one
    # print(student2)
    list_of_passengers = Passenger1.select(Passenger1)
    for passengers in list_of_passengers:
        print(passengers.passenger)

def create_passenger():
    """add a passenger"""
    print("Enter traveler name: "
          "\nPress control-D when finished")
    data = sys.stdin.read().strip()  # read all of the data that comes in
    join_program(data)

def buy_plane_ticket(passenger,program,program2):
    print("Please choose from the following options")
    ticket_choice = input("1.Buy plane ticket\n2.Return to main menu")
    if ticket_choice == "1":
        print("Select airline")
        airline_choice = input("1.Delta Airlines 2.American Airlines")
        number_of_travelers = input("Enter Number of travelers")
        #sammy belongs to 1/delta
        #if the airline choice 1/2 is not airline choice cant be both program 1 and 2
        #if airline choice is not in program 1 or program 2
        if airline_choice not in program:
            if airline_choice not in program2:
                print("Passenger does not belong to this program2")
        if airline_choice not in program2:
            if airline_choice not in program:
                print("Passenger does not belong to this program1234")
        print("Number of miles: {}".format(randint(500, 1500)))
        if airline_choice == "1":
            airline_choice = "Delta Airlines"
        if airline_choice == "2":
            airline_choice = "American Airlines"
        print("Purchased tickets for {} travelers on {}".format(number_of_travelers,airline_choice))

        print(passenger)# passengers name
        print(program2) # 2nd program they joined
        print(program) #first program they joined

def view_entries(search_query = None):
    """View prev entries"""
    list_of_passengers = Passenger1.select(Passenger1)
    # for i in list_of_passengers:
    #     print("full list below")
    #     print(i.passenger)
    # for passengers in list_of_passengers:
    #     print(passengers.passenger)
    # passengers = Passenger1.select().order_by(Entry.timestamp.desc())
    # view entries in order of descending timestamp
    if search_query:
        list_of_passengers = list_of_passengers.where(Passenger1.passenger.contains(search_query))
        # filters so all the entries we select have the content search in their attirbute
        for i in list_of_passengers:
            buy_plane_ticket(i.passenger,i.program,i.program2)
            # print(i.passenger)
            # jill = i.program2
            # if "2" in jill: #instead of if jill.contains("2) WHY?!
            #     print("FUCKERY")
            #     print(jill)

def search_entries():
    """Search entries for a string"""
    list_of_passengers = Passenger1.select(Passenger1)
    print("Select Traveler")
    for i in list_of_passengers:
        print(i.passenger)
    view_entries(input(">Enter Traveler Name"))

def menu_loop():
    while True:
        menuchoice = menuChoice = input("    1.Create Traveler\n    2.Purchase Travel\n    3.Quit\n  >")
        if menuChoice == "1":
           create_passenger()
        if menuChoice == "2":
            search_entries()
        if menuChoice == 3:
            print("cya")
            exit()

if __name__ == '__main__':
    initialize()
    menu_loop()

#use ordered dict and docstrings to control the menu loop to run the methods that
#we need to do

# TODO
# add looping abilities to the adding of a program so they can have 2 programs#
#add a program, ask if theyre done adding a program#
#if done, create the entry with name,program1 info, program2 info = to nothing#
#if not done, ask for second program choice#
# are you finished selecting a program loop#
# print membership details with 1.name 2. programs 3. hotel memb numbers#
#add the ability to create multiple passengers#
#After we print membership details, loop back to main menu#

#Purchase travel menu/options
#select passenger from the list of travelers#
#Buy plane ticket option-->
#if they dont belong to a program, notify them/dont allow "buy plane ticket"#
#if they belong to program, allow them to select airline program to continue#
#Ask for number of travelers, y/n rewards ticket?, number of miles earned
#Display purchased ticket prompt--> Includes passenger name, membership info/number w/...
#...updated miles amount

