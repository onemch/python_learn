class Washer():
    def wash(self):
        print("washing")
        print(self)
    def pringInfo(self):
        print(f'height: {self.height}')


haier1 = Washer()
haier1.height = 120

haier1.pringInfo()