class Washer():
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def printInfo(self):
        print(f'height: {self.height} === width: {self.width}')

    def __str__(self):
        return '洗衣机说明书！！！'

    def __del__(self):
        print('洗衣机已删除！！！')

haier1 = Washer(200,100)
haier1.printInfo()

print(haier1)