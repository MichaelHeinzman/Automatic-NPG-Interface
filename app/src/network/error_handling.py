__all__ = ["handle_error"]

# Helper function for error handling.
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred in function '{func.__name__}': {e}")
            return None
    return wrapper
