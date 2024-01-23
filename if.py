print(45 + 18)#算術演算子　戻り値
print(45 > 18)#比較演算子　戻り値
print("5" == 5)
num1 = 5
num2 = "5"

if num1 == int(num2):
    print("num1とnum2は等しいです")

#------
#ランダムな整数を利用するためrandomモジュールをインポート
import random
#変数numに0~4までのランダムな整数を代入
num = random.randint(0,4)
#変数numの値を出力
print(num)
#変数numのが4であれば大当たりですと出力
if num ==4:
    print("大当たりです")
elif num == 3:
    print("あたりです")
else:
    print("はずれです")

#------
#ランダム整数インポート
import random
#変数numに0~4までをランダムに代入
num = random.randint(0,4)
#変数numを出力
print(num)
#すべての条件が成り立つとき処理（変数numが２)
if 1 < num and num < 3:
    print("変数numは1より大きく、3より小さいです")
else:
    print("and条件が成り立ちませんでした")
#1つでも条件が成り立てば処理する
if num == 1 or num == 3:
    print("変数numは1または3です")
else:
    print("or条件が成り立ちませんでした")