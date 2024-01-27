# datetimeモジュールをインポート
import datetime

# 指定した日時を取得する
date_time = datetime.datetime.strptime("2015-03-19 12:15:30", "%Y-%m-%d %H:%M:%S")

# 取得した日付date_timeの日時を特定のフォーマットで出力する
print(date_time.strftime("%Y年%m月%d日%H時%M分%S秒"))



# datetimeモジュールをインポート
import datetime

# 指定した日時を取得する
date_time = datetime.datetime.strptime("2015-03-19 12:15:30", "%Y-%m-%d %H:%M:%S")

print(date_time)

# 年,月,日,時,分,秒だけをそれぞれ取り出すことも可能です
print(date_time.year)
print(date_time.month)
print(date_time.day)
print(date_time.hour)
print(date_time.minute)
print(date_time.second)



# datetimeモジュールをインポート
import datetime

# 現在時刻を取得する
now = datetime.datetime.now()

# 指定した日時を取得する
date_time = datetime.datetime.strptime("2015-03-19 12:15:30", "%Y-%m-%d %H:%M:%S")

# 2つのdatetimeの差を取得し、変数intervalに代入する（interval＝間隔）
interval = now - date_time

# 取得した日時の差を特定のフォーマットで出力する
print(f"総日数は{interval.days}日です。")



# datetimeモジュールをインポート
import datetime

# 現在時刻を取得する
now = datetime.datetime.now()

# 指定した日時を取得する
date_time = datetime.datetime.strptime("2015-03-19 12:15:30", "%Y-%m-%d %H:%M:%S")

# 2つのdatetimeの差を取得し、変数intervalに代入する（interval＝間隔）
interval = now - date_time

# 取得した日時の差を特定のフォーマットで出力する
print(f"総日数は{interval.days}日です。")