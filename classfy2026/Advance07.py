"""
07.ループと入力 - 複数の数値の合計 4
1 行目で n が入力され、続けて n 行で数値が順に入力されるので、それらの合計を出力してください
"""
n = int(input())
ans = 0
for i in range(n):
    value = int(input())
    ans = ans + value

print(ans)
