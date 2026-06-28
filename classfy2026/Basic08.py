"""
08.N 番目のアルファベット
paiza さんは数字をアルファベットに変換するプログラムを作りたいと考えています。
整数 N が与えられるので、N が 1 であれば A, 2 であれば B のように、辞書順における N 番目のアルファベットを大文字で出力してください。
"""
alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = int(input())
print(alphabet[N])

