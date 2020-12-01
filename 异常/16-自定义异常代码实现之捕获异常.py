class PasswordShortError(Exception):
    def __init__(self,length,min_length):
        self.length = length
        self.min_length = min_length
    def __str__(self):
        return f'你输入的密码长度为{self.length},长度不能小于{self.min_length}'


def main():
    try:
        password = input('请输入密码:')
        if(len(password) < 3):
            raise PasswordShortError(len(password),3)
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')


main()
