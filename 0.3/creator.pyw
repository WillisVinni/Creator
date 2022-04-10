from os import mkdir
from time import sleep
from gui import *
from sys import exit,argv

class project:
    def __init__(self):
        super(project,self).__init__()
        
        self.code={
            'py':"""from sys import exit
# Main function
def main():
    # Any code
    print("Hello, world!")

# If file open not with "open with..." and not as lib
if __name__=="__main__":
    main()
    input(">> ")
    exit()
""",
            'html':"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 style="text-aling: center">Hello, world!</h1>
    <!-- code -->
</body>
</html>
""",
            'bat':"""@echo OFF
SETLOCAL

rem Any code
echo Hello, world!
pause

ENDLOCAL
"""
        }
        
    
    def settings(self,project_name,project_type):
        self.project_name=project_name
        self.project_type=project_type
        self.bat_code=f"""
@echo OFF
SETLOCAL

main.{project_type}
pause

ENDLOCAL
"""
        if project_type in self.code:
            self.file_code=self.code[project_type]
        else:self.file_code=''

    def go(self):
        mkdir(self.project_name)
        sleep(0.2)
        with open(self.project_name+"/main."+self.project_type,'w') as f:
            f.write(self.file_code)

        with open(self.project_name+"/start.bat",'w') as f:
            f.write(self.bat_code)


app = QtWidgets.QApplication(argv)
Window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Window)
Window.show()

def click():
    global ui
    project_name=ui.project_name.text()
    files_type=ui.files_type.text()
    cl=project()
    cl.settings(project_name,files_type)
    cl.go()
    sleep(0.1)
    exit()

ui.pushButton.clicked.connect(click)

exit(app.exec_())