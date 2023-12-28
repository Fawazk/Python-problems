stack = []


def push_stack():
    value = input("Enter the value to push into stack : ")
    stack.append(value)
    print("stack is :", stack, "\n\n\n")


def pop_stack():
    if stack:
        value = stack.pop()
        print("Removed element is :", value, "\n\n")
        print("stack is :", stack, "\n\n\n")
    else:
        print("stack already empty!\n\n\n")


while True:
    choice = int(input("Select 1 to push \nSelect 2 to pop \nSelect 3 to quit\n"))
    if choice == 1:
        push_stack()
    elif choice == 2:
        pop_stack()
    elif choice == 3:
        break
    else:
        print("Select correct operation")
