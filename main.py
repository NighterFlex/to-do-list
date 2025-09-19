def add_task():

def delete_task():

def mark_as_done():

def show_tasks():

def menu():
    
    while True:

        print("\n\n₊˚ ✧ ━━━━⊱ To-do List ⊰━━━━ ✧ ₊˚")
        print("1. Add a Task")
        print("2. Delete a Task")
        print("3. Mark Task as Done")
        print("4. Show Tasks")
        print("5. Exit")

        choice = int(input())

        if choice == 1:
            add_task()
        
        elif choice == 2:
            delete_task()
        
        elif choice == 3:
            mark_as_done()
        
        elif choice == 4:
            show_tasks()
        
        elif choice == 5:
            print("BaiBai :3")
            break

        else:
            print("Invalid input. Try again :<")

        




def main():
    menu()



main()