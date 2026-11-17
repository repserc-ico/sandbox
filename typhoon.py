import base64

#ループ処理を使ってリスト内の要素を表示する
names = ["Damrey","Tianma","Kirogi","Yun-yeung","Koinu",
    "Bolaven","Sanba","Jelawat","Tirou","Maliksi",
    "Gaemi","Prapiroon","Maria","Son-Tinh","Ampil",
    "Wukong","Jongdari","Shanshan","Tomo","Leepi",
    "Bebinca","Pulasan","Soulik","Cimaron","Narae"
]
#for文でループ処理を使えばprint文は1回で済む
for typhoon in names:
    enc_typhoon = base64.b64encode(typhoon.encode("utf-8"))
    typhoon_hash = enc_typhoon.decode("utf-8")
    print(typhoon_hash)
