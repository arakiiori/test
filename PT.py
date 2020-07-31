# coding: shift_jis

import random


test = 0
abcdserfa - 123
member = ["熊","伊織","みるく","わたろ","きるあ","まぁ","まい","たぬ","りお","りょう","せめ","ねさそ","yamyu","ぴゅれ","bb","らべりる","ぴつ","モル"]
count = 0
random.shuffle(member)
for x in member:
	count = count+1
	result = count % 2
	print(x + ":" + str(result))
