import os
from pathlib import Path
import shutil

# Default starting point
documents_path = Path.home() / "Documents"

class App():
    def __init__(self, OS=0, directory=documents_path):
        self.OS = OS
        self.directory = Path(directory)
        self.path = self.directory  # Defaults to directory unless create() is called
        self.file_list = []
        self.index = 0

    @property
    def validate_os(self):
        if not self.OS:
            return "Your Operating system is valid and should support the program"
        else:
            raise SystemError("This application is only supported for windows as of now")
        
    def create(self, name="Organized_Files", create_subfolder=True):
        self.path = self.directory / name
        
        try:
            self.path.mkdir(parents=True, exist_ok=True)
            print(f"Directory '{name}' created/verified at {self.directory}")
            
            if create_subfolder:
                folders = ['Images', 'Documents', 'Videos', 'Apps', 'Audio', 'Code']
                for folder in folders:
                    (self.path / folder).mkdir(exist_ok=True)
        except OSError as error:
            print(f"Directory '{self.path}' could not be created: {error}")
            
    def get_contents(self):
        # Refresh the list each time to avoid duplicates
        if self.path.exists():
            self.file_list = [f.name for f in os.scandir(self.path) if f.is_file()]
        return self.file_list
                         
    def contents(self):
        files = self.get_contents()
        if not files:
            return "The directory is empty or contains only folders."
            
        result = "The files that are in the current directory are:\n"
        for index, file in enumerate(files, start=1):
            result += f"{index}. {file}\n"
        return result
            
    def move_file(self, index, destination):
        # index is 1-based from the contents() display
        self.index = index - 1
        self.destination = Path(destination)
        
        filename = self.file_list[self.index]
        source_path = self.path / filename
        dest_path = self.destination / filename
        
        shutil.move(source_path, dest_path)
        print(f"Moved {filename} to {destination}")

    def sort(self):
        # Map extensions to their target subfolders
        extensions_map = {
            ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
            ".docx": "Documents", ".pdf": "Documents", ".txt": "Documents",
            ".mp4": "Videos", ".mov": "Videos",
            ".exe": "Apps", ".msi": "Apps",
            ".mp3": "Audio", ".wav": "Audio",
            ".py": "Code", ".cpp": "Code", ".html": "Code"
        }

        files = self.get_contents()
        
        for file in files:
            extension = Path(file).suffix.lower()
            if extension in extensions_map:
                target_folder = self.path / extensions_map[extension]
                
                # Ensure the subfolder exists before moving
                target_folder.mkdir(exist_ok=True)
                
                shutil.move(self.path / file, target_folder / file)
                print(f"Sorted: {file} -> {extensions_map[extension]}")