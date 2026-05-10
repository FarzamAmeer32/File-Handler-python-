import os
import shutil


FILE_TYPES = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Music": [".mp3", ".wav"],
            "Documents": [".pdf", ".docx", ".txt"],
            "Videos": [".mp4", ".mkv"],
            "Archives": [".zip", ".rar"],
            'Code':['.cpp','.py']
                            } 

class File_Organizer:
    def __init__(self,path):
        self.path=path
        self.summary={key:0 for key in FILE_TYPES}
        self.summary['Others']=0

    def organize_files(self):
        
        if not os.path.exists(self.path):
            print('No Such Folders Exist')
            return 
        if not os.path.isdir(self.path):
            print('This is not a Folder') 
            return 
               

        files=os.listdir(self.path)    
        
          
        

        for file in files:
            file_path=os.path.join(self.path,file)

            if os.path.isdir(file_path):
                continue

            category='Others'

            ext=os.path.splitext(file)[1].lower()

            for cat,extension in FILE_TYPES.items():
                if ext in extension:
                    category=cat
                    break

            cat_path=os.path.join(self.path,category)
            if not os.path.exists(cat_path):
                os.mkdir(cat_path)

            shutil.move(file_path,os.path.join(cat_path,file))
            self.summary[category]+=1

    def print_summary(self):
        print('Printing Summary of files that have been organized')
        for i,j in self.summary.items():
            print(f'{i} Type organized {j} Times')




path=input('Enter the Folder path you want to Organize\t')
obj=File_Organizer(path)
obj.organize_files()
obj.print_summary()






