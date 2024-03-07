# Import Pakudex and Pakuri class
from pakuri import Pakuri
from pakudex import Pakudex
# Runs if being run from main program
if __name__ == '__main__':
    exit_program = False
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    # Try and exception statement to make sure user enters valid capacity
    max_capacity = 0
    while True:
        try:
            max_capacity = int(input("Enter max capacity of the Pakudex: "))
            if max_capacity < 0:
                raise ValueError
            elif max_capacity > 0 and type(max_capacity) == int:
                break
        except ValueError:
            print("Please enter a valid size.")
        except Exception:
            print("Please enter a valid size.")
    print(f"The Pakudex can hold {max_capacity} species of Pakuri.\n")
    pakudex = Pakudex(max_capacity)
    # While loop to keep running until user wants to exit
    while not exit_program:
        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit\n")
        # Try and exception statement to catch any invalid input from user
        try:
            user_input = int(input("What would you like to do? "))
            # Test case if user wants to list Pukari's in Pakudex
            if user_input == 1:
                species_array = pakudex.get_species_array()
                if species_array is None:
                    print("No Pakuri in Pakudex yet!")
                else:
                    print("Pakuri In Pakudex:")
                    for i in range(pakudex.get_size()):
                        print(f"{i + 1}. {species_array[i]}")
                print()
            # Test case if user wants to see the stats of a specific Pukari in Pakudex
            elif user_input == 2:
                name = input("Enter the name of the species to display: ")
                stats_list = pakudex.get_stats(name)
                if stats_list is None:
                    print("Error: No such Pakuri!")
                else:
                    print("Species:", name)
                    print("Attack:", stats_list[0])
                    print("Defense:", stats_list[1])
                    print("Speed:", stats_list[2])
                print()
            # Test case if user wants to add a Pukari to Pakudex
            elif user_input == 3:
                if pakudex.get_size() == max_capacity:
                    print("Error: Pakudex is full!")
                else:
                    pakuri_name = input("Enter the name of the species to add: ")
                    if pakudex.add_pakuri(pakuri_name):
                        print(f"Pakuri species {pakuri_name} successfully added!")
                    else:
                        print("Error: Pakudex already contains this species!")
                print()
            # Test case for user to evolve specific Pukari Species
            elif user_input == 4:
                evolve_name = input("Enter the name of the species to evolve: ")
                if pakudex.evolve_species(evolve_name):
                    print(f"{evolve_name} has evolved!")
                else:
                    print("Error: No such Pakuri!")
                print()
            # Sorts the Pakudex by Lexicographical ordering
            elif user_input == 5:
                pakudex.sort_pakuri()
                print("Pakuri have been sorted!")
                print()
            # Exits the while loop when user enters 6
            elif user_input == 6:
                print("Thanks for using Pakudex! Bye!")
                break
            # Test case If user inputs number but not 1-6
            else:
                print("Unrecognized menu selection!\n")
        # Exception statement for catching a value error(string instead of int)
        except ValueError:
            print("Unrecognized menu selection!\n")