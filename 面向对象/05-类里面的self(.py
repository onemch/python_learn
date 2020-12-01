class Washer():
    def wash(self):
        print("washing")
        print(self)


haier1 = Washer()

print(haier1)
haier1.wash()

haier1.width = 500

print(f'width:{haier1.width}')


