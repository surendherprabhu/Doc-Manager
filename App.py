import os
from pathlib import Path

documents_path = Path.home() / "Documents"



class App():
    def __init__(self , OS = 0 , directory = documents_path ):
        self.OS = OS
        self.directory = directory
        self.file_list = []
        self.index = 0

    @property
    def validate_os(self):
        if not self.OS:
            return ("Your Operating system is valid and should support the program")
        else:
            raise SystemError("This application is only supported for windows as of now")
        
    def create(self ,name = "Documents"):
         directory = self.directory
         path = os.path.join(directory,name)
         

         try:
             os.mkdir(path)
             print(f"Directory {name} created at {directory} successfully")
             self.new_folder = name
         except OSError as error:
             print(f"Directory '{path}' could not be created: {error}")
        
         with os.scandir(path) as dir:
             if not dir:
                 image = os.path.join(path,"Images")
                 os.mkdir(image)
                 document = os.path.join(path,"Documents")
                 os.mkdir(document)
                 video = os.path.join(path,"Videos")
                 os.mkdir(video)
                 applications = os.path.join(path,"Apps")
                 os.mkdir(applications)
                 audio = os.path.join(path,"Audio")
                 os.mkdir(audio)
                 programming = os.path.join(path,"Code")
                 os.mkdir(programming)
             else:
                 pass
         self.path = path

            
    def get_contents(self):
        self.create()
        with os.scandir(self.path) as dir:
            for element in dir:
                self.file_list.append(element.name)
            return self.file_list
                         
    def contents(self):
         self.file_list_display = self.get_contents()
         result = "The files that are in the current directory are:\n"
         for index , file in enumerate(self.file_list_display , start=1):
            result += f"{index}. {file}" + "\n"
         return result
            
         
    def move_file(self ,index, destination):
         self.index = index
         self.destination = destination

         os.replace(f"{self.directory}/{self.file_list[self.index]}" , f"{self.destination}/{self.file_list[self.index]}")

    def sort(self):
        folder_and_file_list = self.get_contents()
        folder_list = ['Apps', 'Audio', 'Code', 'Documents', 'Images', 'Videos']
        file_list = folder_and_file_list

        for folder in folder_list:
            file_list.remove(folder)
        
        

        
            
        
    
        

        


    