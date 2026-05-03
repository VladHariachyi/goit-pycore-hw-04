from colorama import Fore, Style

from user_events import handle_event, is_user_event


def parse_user_input(user_input: str) -> tuple[str]:
    """Parse the user input.

    Arguments:
    user_input (str) -- The user input.

    Returns:
    parsed_data (tuple[str]) -- Retunrs the tumple, where first item is the command name and rest items are user params.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return (cmd, *args)

def main():
    """ The user manager CLI. Currently supports the Contact Managment functionality."""
    print(f"{Fore.BLUE}Welcome to the assistant bot (^_^){Style.RESET_ALL}")
    contacts = {}

    while(True):
        user_input = input(f"{Fore.YELLOW}Enter a command: {Style.RESET_ALL}")
        command, *args = parse_user_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Fore.YELLOW}Good bye!{Style.RESET_ALL}")
            break

        if command == "hello":
            print(f"{Fore.YELLOW}How can I help you?{Style.RESET_ALL}")
            continue

        if is_user_event(command):
            res = handle_event(command, contacts, *args) 

            if not res is None:
                print(res)

            continue

        print(f"{Fore.RED}The '{command}' command is not supportred!{Style.RESET_ALL}")

        
if __name__ == "__main__":
   main()