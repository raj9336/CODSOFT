task=[]

def add_task():
    task=input("Enter a new task:")
    task.apppend(task)
    print("task added successfully")
def view_task():
    if len(task)==0:
        print("No task to display")
    else:
        print("List of tasks:")
        for i,task in enumerate(task):
            print(f"{i+1}.{task}")

def delete_task():
    if len(task)==0:
        print("No task is deleted")
    else:
        print("task:")
        for i,task in enumerate(task):
            print(f"{i+1}.{task}")
        choice=int(input("Enter the task number to delete"))

        if 0<choice<=len(task):
            del task[choice-1]
            print("Task deleted successfully")
        else:
            print("Invalid task number.")

def main():
    while True:
        print("\n To-Do-List")
        print("___________________")
        print("1.Add Task")
        print("2.View task")
        print("3.Delete Task")
        print("4.Quick")

        choice=int(input("Enter your choice"))
        if choice==1:
            add_task()
        elif choice==2:
            view_task()
        elif choice==3:
            delete_task()
        elif choice==4:
            print("Thank you for using the To-Do-List")
            break
        else:
            print("Invalid choice!Please enter again")
if __name__=="__main__":
    main()                        
               
