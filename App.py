import os
from pathlib import Path

documents_path = Path.home() / "Documents"



class App():
    def __init__(self , OS = 0 , directory = documents_path ):
        self.OS = OS
        self.directory = directory
        self.validate_os()
        self.view_contents()

    def validate_os(self):
        if not self.OS:
            print("yes")
        else:
            raise SystemError("This application is only supported for windows as of now")
        
    def view_contents(self):
        with os.scandir(self.directory) as dir:
            for element in dir:
                with open(f"{self.directory}/{element.name}" , "r") as file:
                    print(file.name)
                    
            
        
    
        

        


    