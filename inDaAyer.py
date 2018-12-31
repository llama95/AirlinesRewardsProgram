from peewee import *
from collections import OrderedDict
import sys
from random import randint

db = SqliteDatabase('Passenger_6rdtry.db')

class Passenger1(Model):

    passenger = CharField(max_length=255, unique=True)
    program = CharField(max_length=255)
    program2 = CharField(max_length=255)
    miles = CharField(max_length=255)
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
                    Passenger1.create(passenger=passeng,program=data,program2=null,miles=0)
                    print("prgram saved succesfully")
            except IntegrityError:
                print("hit integ error1")
                pass
            added_new_passenger(passeng,data,None,0)
        if add_another_program == "y":
            print("Select a frequent flyer travel program to join: \n1.Delta\n2.American"
                  "\nPress control-D when finished")
            data2 = sys.stdin.read().strip()  # read all of the data that comes in
            if data2:
                try:
                    inp = input("save entry y or n ").lower()
                    if inp != "n":
                        Passenger1.create(passenger=passeng, program=data, program2=data2,miles=0)
                        print("Program 2 saved succesfully")
                except IntegrityError:
                    print("hit integ error2")
                    pass
            added_new_passenger(passeng,data,data2,0)
def added_new_passenger(passeng,data,data2,miles=0):
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
    try:
        student = Passenger1.select().order_by(Passenger1.id.desc()).get() #sort Passenger1.id's in desc order, get the first one
        print("Memberships: \n{}\nMembership Number = {}\n{}\nMembership Number = {}".format(data,student,data2,student))
    except IntegrityError:
        print("didnt work")
        print("Nobody in db yet")

def create_passenger():
    """add a passenger"""
    print("Enter traveler name: "
          "\nPress control-D when finished")
    data = sys.stdin.read().strip()  # read all of the data that comes in
    join_program(data)

def buy_plane_ticket(passenger,program,program2,miles):
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
        # miles_var = randint(500,1500)
        # miles_earned = print("Number of miles: {}".format(miles))
        if airline_choice == "1":
            airline_choice = "Delta Airlines"
        if airline_choice == "2":
            airline_choice = "American Airlines"
        rewards_ticket = input("Will this be a rewards ticket y/n?")
        if rewards_ticket == "y":
            print("Select Ticket Type")
            ticket_type = input("1.Domestic 2.Domestic First 3.International")
            if ticket_type == "1":
                if miles < int("2500"):
                    print("failed to reedem award travel. Passenger has {} miles but needs 25000".format(miles))
                else:
                    ticket_type = "Domestic Tickets"
                    if ticket_type == "1":
                        ticket_type = "Domestic Ticket"
                    miles = miles - int("2500")
                    print("Redeemed miles for {} {}".format(miles,ticket_type))
                    list_of_passengers = Passenger1.select(Passenger1)
                    list_of_passengers = list_of_passengers.where(Passenger1.passenger.contains(passenger))
                    for i in list_of_passengers:
                        i.miles = miles
                    update = Passenger1.update(miles=i.miles)
                    update.execute()


        # print("Purchased tickets for {} travelers on {}".format(number_of_travelers,airline_choice))
        print(passenger)# passengers name
        print(program2) # 2nd program they joined
        print(program) #first program they joined
        print(miles) #miles

def view_entries(search_query = None):
    """View prev entries"""
    list_of_passengers = Passenger1.select(Passenger1)
    miles = randint(500, 1500)
    if search_query:
        miles_var = list_of_passengers.where(Passenger1.miles.contains(search_query))
        # for i in miles_var:
        #     print(i.miles)
        list_of_passengers = list_of_passengers.where(Passenger1.passenger.contains(search_query))
        # filters so all the entries we select have the content search in their attirbute
        for i in list_of_passengers:
            print("before update {}".format(i.miles))
            if i.miles == "0":
                print("found zero")
                i.miles = miles
                print(i.miles)
            else:
                print("found not zero")
                i.miles = int(i.miles) + int(miles)
            print(i.miles)
        update = Passenger1.update(miles=i.miles)
        update.execute()
        buy_plane_ticket(i.passenger,i.program,i.program2,i.miles)

#we have our miles attribute of our passenger, if the passenger already has miles from a prev...
#...purchased ticket, we want to add miles from a newly purchased ticket to the miles from the prev purchased ticket
#has to contain the search query and then do the miles shit

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
        if menuChoice == "3":
            print("cya")
            exit()

if __name__ == '__main__':
    initialize()
    menu_loop()

#use ordered dict and docstrings to control the menu loop to run the methods that
#we need to do?

# TODO
#12/27
# add looping abilities to the adding of a program so they can have 2 programs#
#add a program, ask if theyre done adding a program#
#if done, create the entry with name,program1 info, program2 info = to nothing#
#if not done, ask for second program choice#
# are you finished selecting a program loop#
# print membership details with 1.name 2. programs 3. hotel memb numbers#
#add the ability to create multiple passengers#
#After we print membership details, loop back to main menu#
#12/28
#Purchase travel menu/options
#select passenger from the list of travelers#
#Buy plane ticket option-->
#12/29
#if they dont belong to a program, notify them/dont allow "buy plane ticket"#
#if they belong to program, allow them to select airline program to continue#
#Ask for number of travelers, y/n rewards ticket?, number of miles earned#
#Display purchased ticket prompt--> Includes passenger name, membership info/number w/...
#...updated miles amount#
#add miles column to our db#
#12/30
#if they already have miles, add miles from new trip#
#if they have no miles, add the miles#
#add legit rewards numbers for the american and delta rewards programs#
#use proper math when purchasing from domestic,domestic first,international... must have sufficent pts
#add american and delta membership numbers to db... specific memebership numbers tied to specific passengers





