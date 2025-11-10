database = [
    ["REG001", "John Smith", "Car Registration Completed", "Dallas DMV", "Status: Approved"],
    ["TEST002", "Jane Doe", "License Test Scheduled", "Austin DMV", "Date: 11/10/2025, 10:00 AM"]
]

def greet_user():
    fname = input("Please enter your full name: ")
    print(f"Hello, {fname.split()[0]}! Welcome to the DMV Virtual Assistant.")
    return fname

def check_status(ref_num):
    for record in database:
        if record[0] == ref_num:
            print(f"Service: {record[2]}")
            print(f"Location: {record[3]}")
            print(f"Details: {record[4]}")
            return
    print("Record not found. Please check your reference number.")

def register_vehicle():
    print("To register a new vehicle, please bring your title, proof of insurance, and ID to your local DMV.")
    print("You can also start your registration online at: www.dmv.gov/register")

def schedule_test():
    print("Driving tests are available Monday to Friday, 8 AM to 4 PM.")
    print("To schedule your test, visit www.dmv.gov/schedule-test or call 1-800-DMV-TEST.")

def pay_fees():
    print("You can pay your DMV fees securely online at www.dmv.gov/pay.")
    print("Accepted payment methods: Credit Card, Debit Card, or Bank Transfer.")

def contact_support():
    print("Connecting you to a DMV representative...")
    print("You are now connected to customer support.")

def main():
    greet_user()
    ref_num = input("Enter your reference number (if applicable): ").strip().upper()

    while True:
        print("\nWhat would you like to do?")
        print("1. Check status of my registration or test")
        print("2. Register a new vehicle")
        print("3. Schedule a driving test")
        print("4. Pay DMV fees")
        print("5. Contact DMV support")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            check_status(ref_num)
        elif choice == "2":
            register_vehicle()
        elif choice == "3":
            schedule_test()
        elif choice == "4":
            pay_fees()
        elif choice == "5":
            contact_support()
        elif choice == "6":
            print("Thank you for using the DMV Virtual Assistant. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
