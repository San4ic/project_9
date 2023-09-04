def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
    return wrapper

contacts = {}

@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Added {name} with phone number {phone}"

@input_error
def change_phone(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Changed phone number for {name} to {phone}"

@input_error
def get_phone(command):
    _, name = command.split()
    return contacts[name]

def show_all_contacts():
    if not contacts:
        return "No contacts found"
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    while True:
        user_input = input("Enter a command: ").lower()

        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            print(add_contact(user_input))
        elif user_input.startswith("change"):
            print(change_phone(user_input))
        elif user_input.startswith("phone"):
            print(get_phone(user_input))
        elif user_input == "show all":
            print(show_all_contacts())
        else:
            print("Unknown command. Please try again.")

if name == "main":
    main()