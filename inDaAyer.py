from peewee import *
from collections import OrderedDict
import sys

db = SqliteDatabase('Passenger_2ndtry.db')

class Passenger1(Model):

    passenger = CharField(max_length=255, unique=True)
    program = CharField(max_length=255)

    class Meta:
        database = db
def initialize():
    db.connect()
    db.create_tables([Passenger1])
def join_program(passeng) :
    # program_choice = input("Select a frequent flyer travel program to join: \n1.Delta\n2.American")
    """join a program"""
    print("Select a frequent flyer travel program to join: \n1.Delta\n2.American")
    data = sys.stdin.read().strip()  # read all of the data that comes in
    # data = input("Enter traveler name: ")
    if data:
        inp = input("save entry y or n ").lower()
        if inp != "n":
            Passenger1.create(passenger=passeng,program=data)
            print("prgram saved succesfully")


def create_passenger():
    """add a passenger"""
    print("Enter traveler name: ")
    data = sys.stdin.read().strip()  # read all of the data that comes in
    # data = input("Enter traveler name: ")
    # if data:
    #     inp = input("save entry y or n ").lower()
    #     if inp != "n":
    #         Passenger1.create(passenger=data)
    #         print("passenger saved succesfully")
    join_program(data)

def menu_loop():
        menuchoice = menuChoice = input("    1.Create Traveler\n    2.Purchase Travel\n    3.Quit\n  >")
        if menuChoice == "1":
           create_passenger()
        if menuChoice == 2:
            pass #purchase travel
        if menuChoice == 3:
            print("cya")
            exit()
        else:
            print("value is out of range")

if __name__ == '__main__':
    initialize()
    menu_loop()

#use ordered dict and docstrings to control the menu loop to run the methods that
#we need to do
