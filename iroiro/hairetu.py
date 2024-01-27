user_names =  ["侍太郎", "侍一郎", "侍二郎", "侍三郎", "侍四郎"]

print(user_names[1]) #2番目のみ表示

user_names[1] = "侍花子" #2番目を更新
print(user_names)

user_names.append("侍五郎") #6番目を追加
print(user_names)

user_names.pop(2) #3番目を削除(0始まりなので2)
print(user_names)

#-------
country_names = ("日本", "アメリカ", "イギリス", "フランス" )

#3番目を取り出す
print(country_names[2])

#すべてを取り出す
print(country_names)

#-------
country_names = {"アメリカ", "イギリス", "日本", "フランス"}

#セット全体を表示
print(country_names)

# 1～10までに含まれる素数のセット（2と5が重複）
prime_numbers = {2, 5, 2, 7, 3, 5, 5 }

# セット全体を表示
print(prime_numbers)#重複しても大丈夫

#-------
# 1～10までに含まれる素数のセット
prime_numbers = {2, 3, 5, 7}

# セット全体を表示
print(prime_numbers)

prime_numbers.add(11) # 11をセットに追加
print(prime_numbers)

prime_numbers.remove(3) # セットから3を削除
print(prime_numbers)
