class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です。")
        else:
            print(f"{self.name}は大人ではありません。")

# Humanクラスのインスタンスを作成し、リストに追加する
humans = [Human("John Doe", 30), Human("Jane Doe", 18)]

# リストの要素数分だけcheck_adultメソッドを呼び出す
for human in humans:
    human.check_adult()