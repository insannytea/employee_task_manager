#===========TASK MANAGER PROGRAM==========

# TODO make a 'remove task' function

"""
Task Manager is a program built to help small businesses run effectively
by providing a way to organise, add and check employee daily tasks and
check statistics about the current workload
"""

#-----------LIBRARY IMPORT SECTION-----

from datetime import date, datetime



#---------------FUNCTIONS--------------

#.......Reading Data.......

# reads data from tasks.txt and stores it in variable all_tasks
def tasks_read():
    f = open('tasks.txt', 'r+')
    tasks_readlines = f.readlines()
    f.close()
    return tasks_readlines

# reads data from user.txt and stores it in a variable
def user_read():
    f = open('user.txt', 'r+')
    user_readlines = f.readlines()
    f.close()
    return user_readlines

# splits data from user_read() and stores it in a variable as a list
def user_read_split():
    user_read_split = []
    for line in user_read():
        user_read_split += line.split(", ")
    return user_read_split



#.......Creating New Data.......

#---New User Name function---

# reads user input new user name until it doesn't match an existing user name
# returns new user name
def create_new_username():
    # creates a list of data from user.txt
    #user_file_split = user_read_split()
    while True:

        name = input("Please enter a new username:  ")
        print("")

        if name in user_file_split:
            print(f"\nThe user {name} already exists. Please try a different name\n")
            continue
        
        break

    return name
    

#---New Password function---

# reads user input new password and password confirmation until both match
# returns new password
def create_new_password():
    while True:
        password = input("Please enter a new password:  ")
        print("")
        password_confirm = input("Confirm new password: ")
        print("")

        if password != password_confirm:
            print("The passwords don't match. Please try again\n")
            continue

        break

    return password


#---Date Reader function---
def date_input():
    while True:
        deadline_input = input("Please enter the due date(dd/mm/yyyy) of the task:   ")
        print("")
        try:
            deadline = datetime.strptime(deadline_input, "%d/%m/%Y")
            deadline = deadline.strftime("%d %B %Y")
            break

        except ValueError:
            print("\nYou have entered the date in the wrong format. Please try again\n")
    
    return deadline


#---Generating Data for Writing into reports---

def gen_data(a_list):

    total_tasks = 0
    complete_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0

    # counts completed, incomplete and overdue tasks from tasks.txt
    for line in a_list:
        a_list_split = line.split(", ")
        total_tasks += 1

        if a_list_split[-1] == "Yes\n":
            complete_tasks += 1
            continue

        if a_list_split[-1] == "No\n":
            incomplete_tasks += 1
            
        
        # reads and formats deadline date for unfinished tasks
        deadline = datetime.strptime(a_list_split[-2], "%d %B %Y")
        deadline = deadline.date()
        
        # reads and formats current date
        current_date = date.today()

        if deadline < current_date:
            overdue_tasks += 1

    if total_tasks == 0:
        perc_of_complete = 0
        perc_of_incomplete = 0
        perc_of_overdue = 0
    
    else:
        # calculates percentages of incomplete and overdue tasks
        perc_of_complete = round (100 * complete_tasks / total_tasks, 2)
        perc_of_incomplete = round(100 * incomplete_tasks / total_tasks, 2)
        perc_of_overdue = round(100 * overdue_tasks / total_tasks, 2)

    # creates report string
    output = f"Total number of tasks: {total_tasks}\n"
    output += f"Completed tasks: {complete_tasks}\n"
    output += f"Incomplete tasks: {incomplete_tasks}\n"
    output += f"Overdue tasks: {overdue_tasks}\n"
    output += f"Percentage of complete tasks: {perc_of_complete}%\n"
    output += f"Percentage of incomplete tasks: {perc_of_incomplete}%\n"
    output += f"Percentage of overdue tasks: {perc_of_overdue}%\n"

    return output



#......Menu functions.......


#-----Register New User function------

# appends user.txt with new username and new password
def reg_user():
        
    new_login_name = create_new_username()
    new_password = create_new_password()

    new_user = f"{new_login_name}, {new_password}\n"

    user_file.append(new_user)
        
    f = open('user.txt', 'a+')
    f.write(new_user)
    f.close()

    print(f"You have successfully registered {new_login_name}\n")


#------Adding a new task--------

def add_task():

    # checks if user input name exists in user.txt
    while True:
        user_name = input("Enter the USER NAME of the person to assign the task to: ")
        print("")

        if not user_name in user_file_split:
            print("Such user does not exist, please try again\n")
            continue

        break

    # collects data about the task and appends it to the tasks.txt
    task_title = input("Please enter the title of the task: ")
    print("")

    task_description = input("Please enter the description of the task: ")
    print("")

    task_deadline = date_input()


    # reads and formats current date
    current_date = date.today()
    current_date_formatted = current_date.strftime("%d %B %Y")

    new_task = f"{user_name}, {task_title}, {task_description}, {current_date_formatted}, {task_deadline}, No\n"

    all_tasks.append(new_task)

    # appends collected data to tasks.txt file
    f = open('tasks.txt', 'a+')
    f.write(new_task)
    f.close()

    print(f"You have successfully entered a task {task_title} for user {user_name}\n")


#------Viewing All Tasks function-------

def view_all():
    # reads tasks.txt
    # all_tasks = tasks_read()

    # outputs relevant info about each task for all tasks
    for position, line in enumerate(all_tasks, 1):
        all_tasks_split = line.split(", ")

        output = '—'*20 + "{" + f"Task number {position}" + "}" + '—'*20 + '\n'
        output += f"Person responsible:\t{all_tasks_split[0]}\n"
        output += f"Task:\t\t\t{all_tasks_split[1]}\n"
        output += f"Task description:\t{all_tasks_split[2]}\n"
        output += f"Task assigned:\t\t{all_tasks_split[3]}\n"
        output += f"Deadline:\t\t{all_tasks_split[4]}\n"
        output += f"Is completed:\t\t{all_tasks_split[5]}"
        output += '—'*55 + '\n'

        print(output)


#------Viewing My Tasks function-------

def view_mine():
    # reads tasks.txt data to a variable
    # all_tasks = tasks_read()

    task_number = 0
    my_tasks_list = []
    indexing_dictionary = {}

    # outputs tasks assigned to the logged in user name
    for position, line in enumerate(all_tasks, 1):
        all_tasks_split = line.split(", ")

        if all_tasks_split[0] == login_name:
            
            # a list to easily index my tasks
            my_tasks_list.append(all_tasks_split)

            task_number += 1

            # dict key is index of my_tasks_list, value is index of all_tasks
            indexing_dictionary.update({task_number:position})


            output = '—'*20 + f"Task [{task_number}]"+ '—'*20 + '\n'
            output += f"Person responsible:\t{all_tasks_split[0]}\n"
            output += f"Task:\t\t\t{all_tasks_split[1]}\n"
            output += f"Task description:\t{all_tasks_split[2]}\n"
            output += f"Task assigned:\t\t{all_tasks_split[3]}\n"
            output += f"Deadline:\t\t{all_tasks_split[4]}\n"
            output += f"Is completed:\t\t{all_tasks_split[5]}"
            output += '—'*40 + '\n'
            print(output)


    # displays amount of tasks
    # if user does not have any tasks, breaks out of function
    if task_number == 0:
        print("\n> You have no tasks assigned. Enjoy free time! <\n")
        return

    else:
        print(f"You have {task_number} task(s)\n\n")


    # Choose Task or Return to Menu choice part
    
    while True:
        try:
            task_choice = int(input("Enter the number of a task you would like to edit, or '-1' to return to menu:   "))
            print("")

            if task_choice == -1:
                return

            if task_choice <= 0 or task_choice > task_number:
                print(f"\nThere is no task with number {task_choice}. Please try again\n")
                continue

            if my_tasks_list[task_choice - 1][-1] == "Yes\n":
                print("\nSorry, but you can not edit tasks which are finished. Please try a different task\n")
                continue
            
            if task_choice > 0 and task_choice <= task_number:
                break

        except ValueError:
            print("\nSorry, your input has to be a whole number. Please try again\n")
    

    # Edit Task or Mark as Complete choice part

    while True:
        edit_choice = input('''Please choose from the following:\n
et - edit task
mc - mark as completed
em - exit to menu
:   ''').lower()

        # position variables to find exact position in data lists of the selected task
        pos_in_all_tasks = indexing_dictionary[task_choice] - 1
        pos_in_my_tasks = task_choice - 1


        # Editing User Chosen task option
        # only replaces title, description and deadline and writes to tasks.txt
        if edit_choice == 'et':

            task_title = input("Please enter the title of the task: ")
            print("")

            task_description = input("Please enter the description of the task: ")
            print("")

            task_deadline = date_input()


            # formatting data for writing to tasks.txt
            edited_task = f"{my_tasks_list[pos_in_my_tasks][0]}, {task_title}, {task_description}, {my_tasks_list[pos_in_my_tasks][3]}, {task_deadline}, No\n"
            all_tasks.pop(pos_in_all_tasks)
            all_tasks.insert(pos_in_all_tasks, edited_task)
            all_tasks_joined = "".join(all_tasks)

            # writing updated data to tasks.txt
            f = open('tasks.txt', 'w+')
            f.write(all_tasks_joined)
            f.close()


        # Marking User Chosen task as complete option
        elif edit_choice == 'mc':

            # formatting data for writing to tasks.txt

            # changes No to Yes in for user chosen task line
            my_tasks_list[pos_in_my_tasks].pop(5)
            my_tasks_list[pos_in_my_tasks].insert(5, "Yes\n")
            edited_task = ", ".join(my_tasks_list[pos_in_my_tasks])

            # updates the all_tasks list with the new line containing edited_task
            all_tasks.pop(pos_in_all_tasks)
            all_tasks.insert(pos_in_all_tasks, edited_task)
            all_tasks_joined = "".join(all_tasks)

            # writing updated data to tasks.txt
            f = open('tasks.txt', 'w+')
            f.write(all_tasks_joined)
            f.close()

            print(f"\nTask \'{my_tasks_list[pos_in_my_tasks][1]}\' is now marked as completed\n")

        # Returning to Menu option
        elif edit_choice == 'em':
            return

        else:
            print("\n!!!You have made a wrong choice, Please Try again!!!\n")



#------Statistics function------

def view_stats():
    # tries to open and read data from txt file
    # if reading fails, creates txt files and fills with generated data
    try:
        f = open('task_overview.txt', 'r')
        f.close()

        f = open('user_overview.txt', 'r')
        f.close()

    except FileNotFoundError:
        generate_reports()


    # reads data from generated reports text file
    f = open('task_overview.txt', 'r')
    tasks_overview = f.read()
    f.close()

    f = open('user_overview.txt', 'r')
    users_overview = f.read()
    f.close()


    # displays stats
    print("\n\n***STATISTICS***\n\n")
    print(tasks_overview.strip("\n"))
    print(users_overview)

    return


#------Generate Reports function-------

def generate_reports():

    report_data = gen_data(all_tasks)

    # report string stored into task_overview
    f = open('task_overview.txt', 'w')
    f.write(report_data)
    f.close()

    # amount of all users
    total_users = 0

    user_overview_data = []

    # Generates user reports and stores in user_overview.txt file
    # this block generates task data for every user only, general data is inserted later
    for item in user_file_split[::2]:

        total_users += 1
        user_tasks = []

        # checks which tasks in all_tasks belong to user and stores tasks in user_tasks list
        for line in all_tasks:
            all_tasks_split = line.split(", ")
            
            if all_tasks_split[0] == item:
                user_tasks.append(line)
        
        # creates report data for each user from user unique user_tasks list
        report_data = gen_data(user_tasks)
        user_overview_data.append(f"|{item}|\n{report_data}\n")

    # amount of all tasks
    tasks_number = len(all_tasks)

    # data preparation for writing to a text file
    user_overview_data.insert(0, f"Total number of registered users: {total_users}\nTotal number of tasks: {tasks_number}\n\n")
    user_overview_data = "".join(user_overview_data)

    # write data into user_overview.txt
    f = open('user_overview.txt', 'w')
    f.write(user_overview_data)
    f.close()
            
    return

#---Change Password function---

# this function is for changing passwords
# regular users can only change their own password
# admin can change passwords of any user

def change_password():
    
    # admin can change any users password without needing the current password
    if login_name == "admin":
        while True:

            this_name = input("Please enter a username:  ")
            print("")

            if not this_name in user_file_split:
                print(f"\nThe user {this_name} does not exist. Please try a different name\n")
                continue

            break

    
    # regular users have to enter their current password correctly if they want to change password
    else:
        this_name = login_name

        while True:
            user_password = input("Please enter your CURRENT password:  ")
            print("")

            # login_func() returns True if credentials match and so this if statement breaks loop
            if login_func(this_name, user_password):
                break

    
    new_password = create_new_password()

    new_data = f"{this_name}, {new_password}\n"

    # finds the position of user in the list
    pos_in_file = -1
    for line in user_file_split[::2]:
        pos_in_file +=1
        if line == this_name:
            break

    # removes old login data line from the user_file list, inserts new login data line, formats for writing
    user_file.pop(pos_in_file)
    user_file.insert(pos_in_file, new_data)
    user_file_joined = "".join(user_file)

    # writes data into user.txt
    f = open('user.txt', 'w')
    f.write(user_file_joined)
    f.close()
    
    return


def login_func(user, password):
    
    position = -1
    for name in user_file_split[::2]:
        position += 2
        if user == name:
            break
    
    # checks if user name and password match
    password_in_data = user_file_split[position].replace("\n", "")   # cleans text file password from page breaks
    if password_in_data != password:
        print("You have entered wrong credentials. Please try again\n\n")
        output_state = False
    
    # if all credentials match, breaks out of loop
    if user == name and password_in_data == password:
        output_state = True

    return output_state




#.....Misc Functions.....



#-----------WELCOMING SECTION----------

print("\nWelcome to the Task Manager program where you can do stuff with tasks!\n")


#-----------LOGIN SECTION--------------

# converts data from user.txt to a variable
user_file = user_read()
user_file_split = user_read_split()

while True:
    login_name = input("Please enter your USER NAME: ")
    print("")
    user_password = input("Please enter your PASSWORD:  ")
    print("")

    # login_func() returns True if credentials match and so this if statement breaks loop
    if login_func(login_name, user_password):
        break

print(f"\nWelcome back {login_name}!\n\n")

    
#----------------------MENU---------------------


while True:
    user_file = user_read()
    user_file_split = user_read_split()
    all_tasks = tasks_read()

    # gives different menu options for admin and other users
    if login_name == "admin":
        menu = input('''Select one of the following Options below:

ADMIN ACCESS ONLY:
r - Registering a User
st - View Statistics (note: for up-to-date stats, generate reports first with 'gr' option)
gr - Generate Reports
cp - Change Password for Any User

REGULAR ACCESS:
a - Adding a Task
va - View All Tasks
vm - View My Tasks
e - Exit
: ''').lower()
        print("")

    else:
        menu = input('''Select one of the following Options below:

a - Adding a Task
va - View All Tasks
vm - View My Task
cp - Change My Password
e - Exit
: ''').lower()
        print("")


    #------------REGISTERING A NEW USER SECTION-------

    if menu == 'r':
        
        # only admin can access this feature, for other users - outputs error message
        if login_name != "admin":
            print("\n!!!You have made a wrong choice, Please Try again!!!\n")
            continue
        
        reg_user()


    #--------------VIEW STATISTICS SECTION-------------

    elif menu == 'st':
        
        # checks for admin permissions, for other users - outputs error message
        if login_name != "admin":
            print("\n!!!You have made a wrong choice, Please Try again!!!\n")
            continue
        
        view_stats()


    #-------------GENERATE REPORTS SECTION-------------

    elif menu == 'gr':

        # checks for admin permissions, for other users - outputs error message
        if login_name != "admin":
            print("\n!!!You have made a wrong choice, Please Try again!!!\n")
            continue

        generate_reports()
        


    #---------------ADDING NEW TASKS SECTION------------

    elif menu == 'a':

        add_task()


    #----------------VIEW ALL TASKS SECTION-------------

    elif menu == 'va':

        view_all()
        
    
    #---------------VIEW MY TASK SECTION----------------

    elif menu == 'vm':

        view_mine()

    
    #---------------CHANGE PASSWORD SECTION-------------

    elif menu == 'cp':
        change_password()
        print("\nPassword has been successfully changed!\n")
        

    #--------------PROGRAM CLOSE SECTION----------------

    elif menu == 'e':
        print("\nThank you for using Task manager! Goodbye!!!\n")
        exit()

    # error handling for user input outside menu options
    else:
        print("\n!!!You have made a wrong choice, Please Try again!!!\n")