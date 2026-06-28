"""
05.数値演算結果で分岐
整数 A, B, C が与えられます。式 A × B ≦ C が成立している場合はYESを、そうではない場合はNOを出力してください。
"""
A,B,C = map(int, input().split())
if A*B <= C:
    print("YES")
else:
    print("NO")
