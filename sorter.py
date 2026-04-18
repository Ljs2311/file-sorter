import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".tiff", ".tif", ".heic"],

    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".webm", ".flv", ".m4v"],

    "Documents": [".pdf", ".txt", ".rtf", ".md"],

    "Microsoft 365 Word": [".doc", ".docx"],
    "Microsoft 365 Excel": [".xls", ".xlsx"],
    "Microsoft 365 PowerPoint": [".ppt", ".pptx"],

    "Data": [".csv", ".ods", ".odt", ".odp", ".db", ".sqlite", ".sql"],

    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".opus", ".wma", ".alac", ".aiff", ".mid", ".midi"],

    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".cab"],

    "Executables": [".exe", ".msi", ".bat", ".sh"],

    "Code Python": [".py"],
    "Code JavaScript": [".js", ".ts", ".json"],
    "Code Web": [".html", ".css"],
    "Code Backend": [".java", ".cpp", ".c", ".cs", ".php", ".go", ".rs", ".swift", ".rb"],
    "Code Config": [".xml", ".yml", ".yaml"],

    "3D Models": [".obj", ".fbx", ".stl", ".blend", ".3ds"],

    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],

    "Drive Images": [".iso", ".img", ".dmg", ".vhd", ".vmdk", ".qcow2", ".raw", ".vdi"],

    "Installers": [".pkg", ".deb", ".rpm"],

    "Design": [".psd", ".ai", ".xd", ".fig"],

    "Game Files": [".sav", ".rom", ".pak"]
}


def sort_files(folder_path):
    if not folder_path:
        messagebox.showerror("No Folder Selected", "Please select a folder first!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False

        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                destination = os.path.join(folder_path, folder)
                os.makedirs(destination, exist_ok=True)
                shutil.move(file_path, os.path.join(destination, filename))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Other")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))

    messagebox.showinfo("Done", "Files have been sorted successfully!")


def choose_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)


# ---------------- GUI SETUP ----------------

root = tk.Tk()
root.title("File Sorter by: Logan Sneed")
root.geometry("300x200")
root.iconbitmap("favicon.ico")
root.configure(bg="#504949")

folder_path = tk.StringVar()

# ---------------- UI ----------------

label = tk.Label(root, text="Select Folder:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, textvariable=folder_path, width=40)
entry.pack(pady=5)

browse_button = tk.Button(
    root,
    text="Browse",
    command=choose_folder,
    bg="#4CAF50",
    fg="white"
)
browse_button.pack(pady=5)

sort_button = tk.Button(
    root,
    text="Go",
    command=lambda: sort_files(folder_path.get()),
    bg="#2196F3",
    fg="white"
)
sort_button.pack(pady=20)

root.mainloop()