from tkinter import filedialog, Tk
from canvas import Canvas
import pickle

# Function to export shapes to a file
def export_to_file() -> bool:
    # Checking if there are any shapes on the canvas
    if len(Canvas.shapes) <= 0:
        print("No shapes yet")
        return False

    # Asking the user to choose a file for saving
    file_path: str | None = save_file_dialog()

    # Checking if the user cancelled the file selection
    if file_path is None:
        print("Cancelled")
        return False

    # Writing shapes to the chosen file using pickle
    with open(file_path, 'wb') as file:
        pickle.dump(Canvas.shapes, file)

    return True

# Function to open a file dialog and return the selected file path
def open_file_dialog() -> str | None:
    root = Tk()
    root.withdraw()

    file_path: str = filedialog.askopenfilename()
    return file_path if file_path else None

# Function to save a file dialog and return the selected file path
def save_file_dialog() -> str | None:
    root: Tk = Tk()
    root.withdraw()

    # Asking the user to choose a file path and specifying file types
    file_path: str = filedialog.asksaveasfilename(
        defaultextension=".pkl",
        filetypes=[
            ("Pickle", "*.pkl"),
            ("All files", "*.*")
        ]
    )

    return file_path if file_path else None

# Function to import shapes from a file
def import_from_file():
    # Asking the user to choose a file for importing
    file_path = open_file_dialog()

    # Checking if the user cancelled the file selection
    if not file_path:
        print('Cancelled selection')
        return

    # Loading shapes from the chosen file using pickle
    with open(file_path, 'rb') as file:
        Canvas.shapes = pickle.load(file)

