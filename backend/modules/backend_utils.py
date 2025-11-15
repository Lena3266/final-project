"""
Utility functions for the Navi AI backend.
"""

def process_navigation_data(data):
    """Process navigation data from frontend."""
    return {"processed": True, "data": data}

def get_object_info(object_id):
    """Retrieve object information by ID."""
    return {"id": object_id, "info": "object_data"}

def log_event(event_type, event_data):
    """Log events for debugging and analytics."""
    print(f"[{event_type}] {event_data}")
    return True
