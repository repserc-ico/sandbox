"""
08.ループと条件分岐 - 偶奇の判別クエリ 1
1 行目で数値が入力されるので、その数値の回数分標準入力から数値を受け取り、それぞれ"偶数"か"奇数"かを判別して改行区切りで出力してください
"""
num = int(input())
for i in range(num):
    value = int(input())
    if value%2 == 0:
        print("偶数")
    else:
        print("奇数")
