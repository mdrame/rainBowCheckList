
checklist = list() # empty list


def create(item): # this function create / add new stuff to the chicklist list.
    checklist.append(item)
    #print(checklist)


def read(index): # read is being able to access and see an index in a list
    return checklist[index]



def update(index, item): # update checklist function
        checklist[index] = item
        #return checklist



def distory(index): # delete from checklist here
    return checklist.pop(index)
    #print(checklist)

def list_all_items(): # list all code in array/note
    index = 1
    for list_item in checklist:
        print(f" {index} {list_item}") #
        index += 1

# Mark complete
def mark_completed(index): # add color to the output of mark_completed list.

    checklist[index] = "√" + checklist[index]
    return checklist

# Mark incomplete
def not_marked(index):

    checklist[index]= checklist[index][1:len(checklist[index])]
    return checklist



def select(function_code):
    # Create item
    if function_code == "A":
        input_item = input("Add item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(input("Index Number?: ")) # code run's error so yu neddto explicite call init on the imput prompt
        print(read(item_index))
        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "PL":
        list_all_items()

    elif function_code == "D":
        deleted_input = int(input("Index @: "))
        print(distory(deleted_input))

    elif function_code == "U":
        index = int(input("Replace Index: "))
        with_ = str(input("With: "))
        update(index, with_)
        list_all_items()

    elif function_code == "M":
        #list_all_items()
        user_responds = input("Enter C to check and UC to uncheck list: ~ ")

        if user_responds == "C":
            list_all_items()
            checked_index = int(input("Checked in @: ~ "))
            print(mark_completed(checked_index))

        elif user_responds == "UC":
            list_all_items()
            uncheck_index = int(input("Unchecked index @: ~ "))
            print(not_marked(uncheck_index))

        else:
            print("Wrong Key")



    elif function_code == "Q":
        return False #TERMINATE PROGRAME

    # Catch all
    else:
        print("Unknown Option")

    return True

def test(): # THIS IS A TEST FUNCTION ! - - DONT'T CALL IT --``

    create("Black")
    create("White")
    create("Pink")
    create("Blue")
    create("Red")
    print(checklist)
    update(0, "Yellow")
    distory(1)
    list_all_items()



#test() # calling test heere

running = True
while running:
    selection = input(
        "Press A to Add to list, R to Read from list, PL to Display list, U to Update item, D to Destroy item, M to Mark Complete/Incomplete, and Q to quit:\n\n  ~ ")
    running = select(selection)
