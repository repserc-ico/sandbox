"""
07.オリンピックのスコア
テレビをつけると、スキー大会が行われていました。今とあるスポーツ選手の出番が終わり、5 人の審査員から、それぞれ得点が発表されました。i(1 ≦ i ≦ 5) 番目の審査員は、選手の演目に S_i 点の得点を付けました。
このスポーツ選手の最終的な得点は、審査員がつけた得点の最大値と最小値を除いたものの総和になるので、その得点を求めてください。
"""
i = []
for loop in range(1,6):
    score = int(input() )
    i.append(score)
imax = max(i)
imin = min(i)
isum = 0
for loop in i:
    if loop == imax or loop == imin:
        None
    else:
        isum = isum + loop
print(isum)
