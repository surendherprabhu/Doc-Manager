
from DSA import *
import tkinter as tk # Note: usually imported as 'import tkinter as tk'
from tkinter import filedialog, messagebox, scrolledtext
from pathlib import Path
from App import App 

class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer Pro")
        self.root.geometry("600x500")
        
        self.backend = App()
        self.create_widgets()

    def create_widgets(self):
        # --- Directory Selection ---
        tk.Label(self.root, text="Target Directory:", font=("Arial", 10, "bold")).pack(pady=5)
        
        self.dir_frame = tk.Frame(self.root)
        self.dir_frame.pack(fill="x", padx=20) # Fixed: padx instead of px
        
        self.path_entry = tk.Entry(self.dir_frame)
        self.path_entry.pack(side="left", expand=True, fill="x", padx=5) # Fixed: padx
        self.path_entry.insert(0, str(Path.home() / "Documents"))
        
        self.browse_btn = tk.Button(self.dir_frame, text="Browse", command=self.browse_directory)
        self.browse_btn.pack(side="right")

        # --- Action Buttons ---
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=20)

        self.check_os_btn = tk.Button(self.btn_frame, text="Validate OS", command=self.check_os, width=15)
        self.check_os_btn.grid(row=0, column=0, padx=5) # Fixed: padx

        self.create_btn = tk.Button(self.btn_frame, text="Create Folders", command=self.create_folders, width=15)
        self.create_btn.grid(row=0, column=1, padx=5) # Fixed: padx

        self.sort_btn = tk.Button(self.btn_frame, text="Sort Files", command=self.run_sort, width=15, bg="#4CAF50", fg="white")
        self.sort_btn.grid(row=0, column=2, padx=5) # Fixed: padx

        # --- Output Log ---
        tk.Label(self.root, text="Activity Log:", font=("Arial", 10)).pack(pady=5)
        self.log_area = scrolledtext.ScrolledText(self.root, height=15, width=70)
        self.log_area.pack(pady=5, padx=10) # Fixed: padx

    def log(self, message):
        self.log_area.insert(tk.END, f"{message}\n")
        self.log_area.see(tk.END)

    def browse_directory(self):
        selected = filedialog.askdirectory()
        if selected:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, selected)
            self.backend.directory = Path(selected)

    def check_os(self):
        try:
            msg = self.backend.validate_os
            self.log(f"[OS CHECK]: {msg}")
            messagebox.showinfo("OS Status", msg)
        except SystemError as e:
            self.log(f"[ERROR]: {e}")
            messagebox.showerror("OS Error", str(e))

    def create_folders(self):
        # We take the path from the entry box in case the user typed it manually
        self.backend.directory = Path(self.path_entry.get())
        folder_name = "Organized_Files"
        self.backend.create(name=folder_name)
        self.log(f"[CREATE]: Folders created in {self.backend.path}")
        messagebox.showinfo("Success", f"Structure created in {folder_name}")

    def run_sort(self):
        # Safety check: ensures self.backend.path is set
        if not hasattr(self.backend, 'path') or self.backend.path is None:
            self.backend.path = Path(self.path_entry.get())
            
        self.log("[SORT]: Starting sorting process...")
        self.backend.sort()
        
        content_summary = self.backend.contents()
        self.log(content_summary)
        self.log("[SUCCESS]: Sorting Complete.")
        messagebox.showinfo("Done", "Files have been sorted.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = AppGUI(root)
    root.mainloop()