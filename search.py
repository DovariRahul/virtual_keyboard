import webbrowser
import pyautogui
import time

def handle_search(search_text=None):
    """
    Opens Google search with the given text.
    If no text provided, it assumes the user has typed something in active field.
    """
    if search_text:
        # Open Google search directly
        query = search_text.replace(" ", "+")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
    else:
        # If no text provided, simulate pressing Enter in browser/search field
        pyautogui.press("enter")
        # Optional: small delay to let browser process
        time.sleep(0.1)
