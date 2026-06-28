"""
10.背の順
保健係のあなたは名前と身長のリストを身長が高い順に並べなおすようお願いされました。
生徒の数 N, i 番目の生徒の名前 S_i、i番目の生徒の身長 A_i が与えられます(1 ≦ i ≦ N)。
身長が高い生徒から順に改行区切りで名前を出力してください。
"""
N = int(input())
data = []
for i in range(0,N):
    H, NM = input().split()
    data.append( (int(H), NM) )
data.sort()
for height,name in data:
    print(name)
