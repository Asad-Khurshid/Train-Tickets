#importing modules
import sys

#Defining function for reeserving seats
def reservation(number_of_tickets, maxKey):
    dict = {}
    for n in range(maxKey + 1, maxKey + number_of_tickets+1):
        name = input("Enter person's Name: ")
        age = input("Enter person's Age: ")
        gender = input("Enter person's Gender: ")
        dict[n] = [name, age, gender]
    return dict

#Defining function for printing all reserved seats
def generate_all_tickets(dict):
    for seat in dict:
        x = dict[seat]
        print ("Ticket no:", seat, "is reserved for:", x[0], "Age:", x[1], "Gender:", x[2])

#Defining main function
def main():
    decision = 0
    reserved_tickets = {}
    #initiating while loop to keep the porgram running
    while True:
        decision = input("If you want to reserver Tickets, Press 1.\nIf you want to generate all tickets, Press 2.\nIf you want to end the program, Enter end.\nType here: ")
        if decision == "end":
            sys.exit()
        if int(decision) == 1:
            n_tickets = input("Enter the number of tickets you want to reserve: ")
            try:
                max_key = max(reserved_tickets, key=reserved_tickets. get)
                print (max_key)
            except:
                max_key = 0
            tempDict = reservation(int(n_tickets), int(max_key))
            reserved_tickets.update(tempDict)
        elif int(decision) == 2:
            print(generate_all_tickets(reserved_tickets))

#Executing program
if __name__ == "__main__":
    main()