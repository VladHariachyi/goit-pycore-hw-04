from .user_events_constants import USER_CONTACT_EVENTS, USER_EVENTS
from .contact_event_handler import handle_contact_event


def is_user_event(event_name: str) -> bool:
    """Check if event is the user event.

    Arguments:
    event_name (str) -- The user event name.

    Returns:
    is_user_event (bool) -- The validation result.
    """
    return event_name in USER_EVENTS

def is_contact_event(event_name: str) -> bool:
    """Check if event is related to Contact Manager events.

    Arguments:
    event_name (str) -- The user event name.

    Returns:
    is_contact_event (bool) -- The validation result.
    """
    return event_name in USER_CONTACT_EVENTS

def handle_event(
    event_name: str, 
    data_store: dict[str, str] | None, 
    *args: tuple[str]
) -> str | None:
    """User events handler.

    Arguments:
    event_name (str) -- The user event name. Currently events for Contact Maager are supported.

    data_store (dict[str, str] | None) -- The data store which will be processed by event handlers.

    args (tuple[str]) -- The event params. 

    Returns:
    result (str | None) -- Returns result of event handler execution.
    """
    if is_contact_event(event_name):
        contact_name = None
        phone = None

        if len(args) == 2:
            contact_name, phone = args
        elif len(args) == 1:
            contact_name = args[0]
        
        contact_data = { "name": contact_name, "phone": phone } if args else None

        return handle_contact_event(event_name, data_store, contact_data)