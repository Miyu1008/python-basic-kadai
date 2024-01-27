class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Humanクラスのインスタンスを作成し、変数に代入する
person = Human("侍太郎", 30)

# printinfoメソッドを呼び出す
person.printinfo()