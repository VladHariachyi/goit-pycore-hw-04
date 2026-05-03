from colorama import Fore, Style
import re


def is_phone_number_valid(phone_number: str) -> bool:
    """Validates the entered phone number

    Arguments:
    phone_number (str) -- The phone number to validate.

    Returns:
    is_valid (bool) -- The validation result.
    """
    return not re.match(r"^(\+380)\d{9}$", phone_number) is None

def is_contact_name_valid(contact_name: str) -> bool:
    """Validates the entered contact name

    Arguments:
    contact_name (str) -- The contact name to validate.

    Returns:
    is_valid (bool) -- The validation result.
    """
    return contact_name.isalpha()

def add_contact(contact_name: str, phone_number: str, contacts: dict[str, str]) -> str | None:
    """Add contact to the contacts storage.

    Arguments:
    contact_name (str) -- The contact name.
    phone_number (str) -- The contact phone number.
    contacts (dcit[str, str]) -- The contacts storage.

    Returns:
    result (str | None) -- Returns string with success message about added a new contact.
    "None" is returned if error happened.
    """
    if (not (contact_name or phone_number)):
        print((
            f"{Fore.RED}The Contact Manager Error: Is not possible to add "
            f"the new contact due to missed arguments{Style.RESET_ALL}"
        ))
        return None
    
    if contacts.get(contact_name.lower()):
        print( f"{Fore.RED}The Contact Manager Error: The user '{contact_name}' already exists")
        return None
    
    if not is_contact_name_valid(contact_name):
        print((
            f"{Fore.RED}The Contact Manager Error: The user '{contact_name}' "
            f"is not valid, use only alphabetical characters{Style.RESET_ALL}"
        ))
        return None


    if not is_phone_number_valid(phone_number):
        print((
            f"{Fore.RED}The Contact Manager Error: The provided phone number is not valid,"
            f" use following format '+380000000000'{Style.RESET_ALL}"
        ))
        return None
    
    contacts[contact_name.lower()] = phone_number

    return f"{Fore.GREEN}The '{contact_name}' was successfully added to the contacts{Style.RESET_ALL}"

def change_contact(contact_name: str, phone_number: str, contacts: dict[str, str]) -> str | None:
    """Change existing contact phone number.

    Arguments:
    contact_name (str) -- The contact name.
    phone_number (str) -- The contact phone number.
    contacts (dcit[str, str]) -- The contacts storage.

    Returns:
    result (str | None) -- Returns string with success message about changing the contact phone number.
    "None" is returned if error happened.
    """
    if (not (contact_name or phone_number)):
        print((
            f"{Fore.RED}The Contact Manager Error: Is not possible to change the"
            f"contact due to missed arguments{Style.RESET_ALL}"
        ))
        return None
    
    if is_phone_number_valid(phone_number):
        if contacts.get(contact_name.lower()):
            contacts[contact_name.lower()] = phone_number
            return f"{Fore.GREEN}The phone number was sucessfully changed for {contact_name}{Style.RESET_ALL}"
        else:
            print(f"{Fore.RED}The Contact Manager Error: {contact_name} is missing in contacts{Style.RESET_ALL}")
            return None 
    
    print((
        f"{Fore.RED}The Contact Manager Error: The provided phone number is not valid,"
        f" use following format '+00000000000'{Style.RESET_ALL}"
    ))
    return None

def show_phone(contact_name: str, contacts: dict[str, str]) -> str | None:
    """Show contact phone number by contact name.

    Arguments:
    contact_name (str) -- The contact name.
    contacts (dcit[str, str]) -- The contacts storage.

    Returns:
    result (str | None) -- Returns string with contact phone number.
    "None" is returned if error happened.
    """
    try:
        return (
            f"{Fore.BLUE}{contact_name} has following phone number: "
            f"{contacts[contact_name.lower()]}{Style.RESET_ALL}"
        )
    except KeyError:
        print(f"{Fore.RED}{contact_name} doest not exist{Style.RESET_ALL}")
        return None

def show_all(contacts: dict[str, str]) -> str:
    """Show all contacts saved to the storage..

    Arguments:
    contacts (dcit[str, str]) -- The contacts storage.

    Returns:
    result (str) -- Returns string with info about all contacts.
    """
    contacts_info = ""

    for contact in contacts:
        contacts_info += (
            f"{Fore.BLUE}{contact.title()} has following phone number: "
            f"{contacts[contact]}\n{Style.RESET_ALL}"
        )

    return contacts_info