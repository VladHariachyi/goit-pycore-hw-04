from colorama import Fore, Style

from contact_manager import add_contact, show_phone, change_contact, show_all


def handle_contact_event(
    event_name: str, 
    contacts: dict[str, str], 
    contact_data: dict[str, str | None] | None = None
) -> str | None:
    """Contacts events handler.

    Arguments:
    event_name (str) -- The contact manager event name, supported events: "add_contact",
    "change_contact", "show_phone", "show_all_contacts"

    contacts (dict[str, str]) -- The contacts storage.

    contact_data (dict[str, str | None] | None) -- Contact data, consits of "name" and "phone" fields.
    Some event handlers do not require full definition of contact data. 

    Returns:
    result (str | None) -- Returns result of event handler execution.
    """
    if contacts is None:
        print(f"{Fore.RED}The Contact Manager Error: The 'contants' storage is not provided{Style.RESET_ALL}")
        return None
    
    contact_data = contact_data or {}

    match event_name:
        case 'add_contact':
            return add_contact(contact_data.get("name"), contact_data.get("phone"), contacts)
        case 'change_contact':
            return change_contact(contact_data.get("name"), contact_data.get("phone"), contacts)
        case 'show_phone':
            return show_phone(contact_data.get("name"), contacts)
        case 'show_all_contacts':
            return show_all(contacts)