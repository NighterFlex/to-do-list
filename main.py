import json
import os

tasks = []

FILENAME = "tasks.json"

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent= 3)


def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            tasks = json.load(f)
    else:
        tasks = []

def add_task():
    task_num = int(input("How many tasks do you wanna add? :3 \n"))

    for i in range(task_num):
        task = input("Enter your task: ")
        tasks.append({"task" : task, "done" : False})
        print("Your task has been added~")
    
    save_tasks()

def show_tasks():
    if not tasks:
        print("Nothing to see here :<")
        return

    print("\nYour Tasks:")

    status = ""
    for j in range(len(tasks)):
        if tasks[j]["done"]:
            status = "yay ✓"
        else:
            status = "nay ✗"

        print(f"{j+1}. {tasks[j]['task']} {status}")

def delete_task():
    
    show_tasks()

    del_index = int(input("Enter the task number you want to delete: "))
    if 1 <= del_index <= len(tasks):
        del tasks[del_index - 1 ]                       #since indexing starts from 0 butttt, we want it to start from 1 :3
        print("Task deleted! :3")

        save_tasks()
    
    else:
        print("Invalid task number :<")


def mark_as_done():
    show_tasks()

    mark_index = int(input("Enter the task number to mark as done: "))

    if 1 <= mark_index <= len(tasks):
        tasks[mark_index - 1]["done"] = True
        print("Your task has been marked as done uwu")

        save_tasks()
    
    else:
        print("Invalid task number :<")

def menu():
        print("\n\n₊˚ ✧ ━━━━⊱ To-do List ⊰━━━━ ✧ ₊˚")
        print("1. Add a Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete a Task")
        print("5. Exit")



def main():

    load_tasks()

    while True:
        menu()
        choice = int(input())

        if choice == 1:
            add_task()

        elif choice == 2:
            show_tasks()
        
        elif choice == 3:
            mark_as_done()
        
        elif choice == 4:
            delete_task()

        
        elif choice == 5:
            print("BaiBai :3")
            break

        else:
            print("Invalid input. Try again :<")
            continue

        RE = input("Do you wanna go to the main menu :3 (y/n)\n").lower()
        if RE != "y":
            print("BaiBai :3")
            break



main()