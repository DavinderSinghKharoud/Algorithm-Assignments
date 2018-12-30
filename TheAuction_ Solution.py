# Enter your names and ids as comment here
# [Davinder Singh Kharoud] - [1893033]
# [Jagdeep Singh] - [1893739]
# [Vivek Kumar] - [1893481]

"""
PROBLEM

A small town is organizing an auction to finance building an arena for community sports. The auction has caught a
lot of media attention and so the organizer believe they will need to computerize their inventory.

They are asking you to write a simple program which will prompt the user for commands to handle the inventory.

The program should be able to do the following:

- Add an item to the inventory
- Remove an item from the inventory
- Print the inventory
- Exit and save the inventory to a text file

The program should not be case sensitive with regard to item names.

Moreover, for both computer and human efficiency, the inventory should be kept sorted at all time.

See the pdf of the work for more details

CODING

You are given a basic skeleton of what your app code will look like. Some function have been created for you but left
empty.

You will likely have to write more functions. Make sure your code is well organized
"""

# ======================================================================================================================
#  Helper functions
# ======================================================================================================================

def binary_search(inventory, item):
    low = 0
    high = len( inventory ) - 1
    while low <= high:
        lookup = round( (low + high) / 2 )
        if inventory[lookup] < item:
            low = lookup + 1
        elif inventory[lookup] > item:
            high = lookup - 1
        else:
            return lookup
    return None


# ======================================================================================================================
#  Inventory management
# ======================================================================================================================

def add(inventory, item):
    if len(inventory)==0:
        inventory.append(item.title())
    else:
        titleCase=item.title()
        count=0
        for element in range(len(inventory)-1,-1,-1):
            if inventory[element]<titleCase:
                count+=1

        inventory.insert(count,titleCase)
    return inventory



def remove(inventory, item):
    value=binary_search(inventory,item)
    if value is not None:
       del inventory[value]
       return inventory



# ======================================================================================================================
#  Inventory formatting
# ======================================================================================================================

def inventory_to_string(inventory):
    """
    Format the inventory and return it. This function should not print the inventory.
    Ex: the inventory ['Boat', 'Guitar' 'Shoes'] returns the string:
    1) Boat
    2) Guitar
    3) Shoes
    """
    strng = "Here are the items in the inventory: \n"
    for i in range(len(inventory)):
        strng+="{}) ".format(i+1)+inventory[i]+"\n"
    return strng



# ======================================================================================================================
#  Output
# ======================================================================================================================

def save(inventory, filename):
    value=inventory_to_string(inventory)
    with open (filename,'w+') as file:
                file.write(value)

def print_inventory(inventory):
   pasting=inventory_to_string(inventory)
   return pasting


# ======================================================================================================================
#  Main function
# ======================================================================================================================

def main():
    inventory = []
    print("== Welcome to the Auction! ==")
    while True:
        user=input('Please enter a command ( "add" , "remove" , "print" or "exit".)\n>>>')
        if user=="add":
            user1 = input( "Name the item you want to add.\n>>>" )
            value=add(inventory,user1)
            print("You added {} to the inventory.".format(user1.title()))
        elif user=="remove":
            user2=input("Name the item you want to remove.\n>>>")
            remove(inventory,user2.title())
            print("You removed {} from the inventory.".format(user2.title()))
        elif user=="print":
            printing=print_inventory(inventory)
            print(printing)
        elif user=="exit":
            save(inventory,'items.txt')
            print("Your inventory will be saved to 'items.txt' . Goodbye !")
            break







# That is a convention in Python, do not touch the lines below
if __name__ == '__main__':
    main()
