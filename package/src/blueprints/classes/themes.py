class Themes(object):
    # Класс для изменения темы
    def __init__(self):
        self.theme_mode = 1

    def change_mode(self):
        if self.theme_mode < 3:
            self.theme_mode = self.theme_mode + 1
        else:
            self.theme_mode = 1