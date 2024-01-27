# 与えられた引数$priceに送料を加算し、その値を出力する関数を定義する
def calculate_total(price,shipping_fee):
    # 与えられた引数priceに送料を加算し、変数totalに代入する
    total = price + (price * shipping_fee)/100

    # 変数totalの値を出力する
    print(f"{total}円")

# 関数を呼び出し、引数として購入金額を渡す
calculate_total(1200,10)