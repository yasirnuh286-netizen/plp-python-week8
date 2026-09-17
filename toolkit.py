import random

def run_number_guessing_game():
    """
    Tool 1: Number-Guessing Game
    Uses loops, conditionals, and f-strings.
    Generates a random number and gives feedback until the user guesses correctly.
    """
    secret_number = random.randint(1, 20)
    attempts = 0
    print("\n--- 🎯 Number-Guessing Game ---")
    print("I'm thinking of a number between 1 and 20.")
    
    while True:
        user_input = input("Take a guess (or type 'cancel' to exit): ")
        if user_input.lower() == 'cancel':
            print("Game cancelled. Returning to main menu.")
            break
            
        if not user_input.isdigit():
            print("❌ Please enter a valid whole number!")
            continue
            
        guess = int(user_input)
        attempts += 1
        
        if guess < secret_number:
            print(f"Too low! Try higher than {guess}.")
        elif guess > secret_number:
            print(f"Too high! Try lower than {guess}.")
        else:
            print(f"🎉 Congratulations! You guessed the secret number {secret_number} in {attempts} attempt(s)!")
            break


def run_todo_list():
    """
    Tool 2: Interactive To-Do List
    Uses dynamic lists, loops, conditionals, and f-strings.
    Allows users to view, add, and remove tasks dynamically.
    """
    tasks = []
    print("\n--- 📋 Interactive To-Do List ---")
    
    while True:
        print("\nTo-Do Sub-Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Return to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            if not tasks:
                print("Your to-do list is currently empty!")
            else:
                print("\nYour Current Tasks:")
                for idx, task in enumerate(tasks, 1):
                    print(f"  {idx}. {task}")
        elif choice == '2':
            new_task = input("Enter the new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"✅ Added task: '{new_task}'")
            else:
                print("❌ Task cannot be empty!")
        elif choice == '3':
            if not tasks:
                print("❌ No tasks available to remove!")
                continue
            
            print("\nCurrent Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"  {idx}. {task}")
                
            task_num = input("Enter the number of the task to remove: ").strip()
            if task_num.isdigit():
                idx_to_remove = int(task_num) - 1
                if 0 <= idx_to_remove < len(tasks):
                    removed = tasks.pop(idx_to_remove)
                    print(f"🗑️ Successfully removed: '{removed}'")
                else:
                    print("❌ Invalid task number!")
            else:
                print("❌ Please enter a valid number.")
        elif choice == '4':
            print("Exiting To-Do List...")
            break
        else:
            print("❌ Invalid choice! Please select an option between 1 and 4.")


def run_tip_calculator():
    """
    Tool 3: Simple Tip Calculator
    Uses conditionals, math formatting, and f-strings.
    Calculates total tip and per-person cost for splitting a bill.
    """
    print("\n--- 💡 Simple Tip Calculator ---")
    try:
        bill_amount = float(input("Enter total bill amount ($): "))
        tip_percent = float(input("Enter tip percentage (e.g., 15, 18, 20): "))
        people_count = int(input("How many people are splitting the bill? "))
        
        if bill_amount < 0 or tip_percent < 0 or people_count <= 0:
            print("❌ Please enter positive values and at least 1 person.")
            return
            
        tip_amount = bill_amount * (tip_percent / 100)
        total_bill = bill_amount + tip_amount
        cost_per_person = total_bill / people_count
        
        print(f"\n--- Calculation Results ---")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Bill: ${total_bill:.2f}")
        print(f"Each person owes: ${cost_per_person:.2f}")
    except ValueError:
        print("❌ Invalid numerical input. Returning to main menu.")


def main():
    """
    Main menu loop handling program flow, non-crashing options, and clean exits.
    """
    print("============================================")
    print("👋 Welcome to your Personal Mini-Toolkit!")
    print("============================================")
    
    while True:
        print("\n====================================")
        print("      PERSONAL MINI-TOOLKIT         ")
        print("====================================")
        print("1. Play Number-Guessing Game")
        print("2. Open Interactive To-Do List")
        print("3. Launch Simple Tip Calculator")
        print("4. Quit Program")
        print("====================================")
        
        user_choice = input("Enter your choice (1-4): ").strip()
        
        if user_choice == '1':
            run_number_guessing_game()
        elif user_choice == '2':
            run_todo_list()
        elif user_choice == '3':
            run_tip_calculator()
        elif user_choice == '4':
            print("\n👋 Thank you for using Personal Mini-Toolkit! Goodbye!")
            break
        else:
            print(f"\n❌ '{user_choice}' is not a valid option! Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()