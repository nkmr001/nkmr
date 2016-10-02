#coding:utf-8
import time,sys,datetime,math

count = raw_input("周回回数を書き込んでください>>")
c = 0
count_list = []
while True:
	abc = raw_input("クエストスタートボタンを押したらエンターを押してください")
	start = time.time()
	a = raw_input("報酬を受け取ったらエンターを押してください")
	c+=1
	stop = time.time() - start
	count_list.append(math.ceil(stop))
	print("\n今のは"+str(c)+"回目です周回にかかった時間は"+str(math.ceil(stop))+"秒です\n")
	if str(count) == str(c):
		lis = int(sum(count_list)) / int(count)
		print("終わりましたお疲れ様でした\n平均周回時間は"+str(lis)+"秒です")
		sys.exit()