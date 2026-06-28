"""
09.ループと条件分岐 - フィルタリング 1
1 行目に数値が入力されるので、その数値の回数分標準入力から数値を受け取り、それぞれ 5 の倍数のものだけを改行区切りで出力してください
"""
num = int(input())
for i in range(num):
    value = int(input())

    if value % 5 == 0:
        print(value)
