def show_user_name():
    # ローカル変数を定義する
    user_name = "侍太郎"

    # ローカルスコープの範囲内でローカル変数を使う
    print(user_name)

show_user_name()





# グローバル変数を定義する
user_name = "侍花子"

def show_user_name():
    # ローカル変数を定義する
    user_name = "侍太郎"

    # ローカルスコープの範囲内でローカル変数を使う
    print(user_name)

show_user_name()

# グローバルスコープの範囲内でグローバル変数を使う
print(user_name)
