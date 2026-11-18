import base64

#ループ処理を使ってリスト内の要素を表示する
names = ["Damrey*","Tianma*","Kirogi*","Yun-yeung*","Koinu*",
    "Bolaven*","Sanba*","Jelawat*","Tirou*","Maliksi*",
    "Gaemi*","Prapiroon*","Maria*","Son-Tinh*","Ampil*",
    "Wukong*","Jongdari*","Shanshan*","Tomo*","Leepi*",
    "Bebinca*","Pulasan*","Soulik*","Cimaron*","Narae*"
]
counter = 0
#ループ処理を使って配列の要素とそのハッシュ値を出力
for typhoon in names:
    counter += 1
    enc_typhoon = base64.b64encode(typhoon.encode("utf-8"))
    typhoon_hash = enc_typhoon.decode("utf-8")
    print(f"{counter}:{typhoon}")
    print(typhoon_hash)
