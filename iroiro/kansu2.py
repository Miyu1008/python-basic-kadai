# 与えられた引数$priceに送料を加算し、その値を出力する関数を定義する
def calculate_total(price):
    # 与えられた引数priceに送料を加算し、変数totalに代入する
    total = price + 500

    # 変数totalの値を出力する
    print(f"{total}円")

# 関数を呼び出し、引数として購入金額を渡す
calculate_total(1200)

def add_two_arguments(price, shipping_fee):
    # 与えられた引数priceと引数shipping_feeを加算し、変数totalに代入する
    total = price + shipping_fee

    # 変数$totalの値を出力する
    print(f"{total}円")

# 関数を呼び出し、引数として購入金額と送料を渡す
add_two_arguments(1200, 500)