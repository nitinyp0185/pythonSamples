from time import sleep


class AppController:
    def __init__(self, app):
        self.app = app

    def quitApp(self):
        print("Application is quitting...")
        sleep(2)
        self.app.quit()