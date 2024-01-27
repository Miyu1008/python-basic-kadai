def calculate_total(price, shipping_fee):
    # 与えられた引数priceに送料を加算し、変数totalに代入する
    total = price + (price * shipping_fee) / 100

    # 変数totalの値を戻り値として返す
    return total

# 関数を呼び出し、引数として購入金額と送料を渡す
total_price = calculate_total(1200, 10)

# 戻り値を出力する
print(f"{total_price}円")