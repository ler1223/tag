from DB import get_name


class User():
    def __init__(self):
        self.name_f = "user.txt"
        self.name = "Гость"
        self.login = "---"
        self.name_image = "default_image/CR_TCDM_dump40_400_170000_12000_100_blue.png"

    def entrance_user(self, email):
        self.name = get_name(email)
        self.login = email
        name, email, name_image = self.read_f()
        self.write_f(self.name, self.login, name_image)

    def guest(self):
        self.name = "Гость"
        self.login = "---"
        name, email, name_image = self.read_f()
        self.write_f(self.name, self.login, name_image)

    def get_name(self):
        file = open(self.name_f, mode="r")
        name = str(file.readlines()[0]).strip()
        return name

    def set_name_image(self, name_image):
        print(self.read_f())
        name, email, name_image_f = self.read_f()
        self.write_f(name, email, name_image)

    def get_name_image(self):
        return self.read_f()[2]

    def read_f(self):
        file = open("user.txt", mode="r")
        lines = file.readlines()
        name = lines[0].strip()
        email = lines[1].strip()
        name_image = lines[2].strip()
        return name, email, name_image

    def write_f(self, name, email, name_image):
        self.name = name
        self.name_image = name_image
        self.login = email
        file = open(self.name_f, mode="w")
        file.write(self.name + "\n")
        file.write(self.login + "\n")
        file.write(self.name_image)
        file.close()
