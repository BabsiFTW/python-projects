"""1. Print a welcome message to the user
2. Prompt the user to view, add, update, or delete an event on the calendar
3. Depending on the user's input: view, add, update, or delete an event on the calendar
4. The program should never terminate unless the user decides to exit
"""
from time import sleep, strftime
first_name = "Barbara"
calendar = {}
def welcome():
  print "Hello %s" % (first_name)
  print "Calendar is opening..."
  sleep(1)
  strftime("%A %b %d, %Y")
  strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"
def start_calendar():
    welcome()
    start = True
    while start:
      user_choice = raw_input("Add A to Add, U to Update, V to View, D to Delete, X to Exit: ")
      user_choice = user_choice.upper()
      
      #Option of viewing the calendar
      if user_choice == "V":
        if len(calendar.keys()) == 0:
          print "Calendar is empty!"
        #else:
        else:
         print calendar
        
      #Option of updating the calendar
      elif user_choice == "U":
        date = raw_input("What date? ")
        update = raw_input("Enter the update: ")
        calendar[date] = update
        print calendar
        print "Update was successfull!"
      
      #Option of adding events to the calendar
      elif user_choice  == "A":
        event = raw_input("Enter event: ")
        date = raw_input("Enter date (MM/DD/YYYY): ")
        if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
          print "Invalid date was entered!"
          try_again = raw_input("Try again? Y for Yes, N for No: ")
          try_again = try_again.upper()
          if try_again == "Y":
            continue
          else:
            start = False
        else:
          calendar[date] = event
          print "Event was sucessfully added!"
          print calendar  
      
      #Option of deleting events in the calendar
      elif user_choice == "D":
        if len(calendar.keys()) < 1:
          print "Error! YOur calendar is empty!"
        else:
          event = raw_input("What event? ")
          for date in calendar.keys():
            #using keys()?
            if event == calendar[date]:
              del calendar[date]
              print "Event was succesfully deleted!"
              print calendar
            else:
              print "An incorrect event was specified!"
      
      #Enables user to exit the program
      elif user_choice == "X":
        start = False
      else:
        print "An invalid command was entered!"
        start = False
start_calendar()
