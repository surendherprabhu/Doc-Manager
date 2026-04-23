import os
from pathlib import Path

documents_path = Path.home() / "Documents"



class App():
    def __init__(self , OS = 0 , directory = documents_path ):
        self.OS = OS
        self.directory = directory
        self.file_list = []
        self.index = 0

        print(self.validate_os)
        self.get_contents()
        self.display_contents(self.file_list)
        self.move_file(1, "sample")

        

    @property
    def validate_os(self):
        if not self.OS:
            return ("Your Operating system is valid and should support the program")
        else:
            raise SystemError("This application is only supported for windows as of now")
        
    def get_contents(self):
        with os.scandir(self.directory) as dir:
            for element in dir:
                    if "." in element.name:
                         self.file_list.append(element.name)
                         

    def display_contents(self , file_list_display):
         self.file_list_display = file_list_display
         for index , file in enumerate(self.file_list_display , start=1):
              print(f"{index}. {file}")
              
         
    def move_file(self ,index, destination):
         self.index = index
         self.destination = destination

         os.replace(f"{self.directory}/{self.file_list[self.index]}" , f"{self.destination}/{self.file_list[self.index]}")
              
                    
            
        
    
        

        


    