def split(x):
	x = x.split(",")
	school = x[0].replace("我是","")
	print(f"學校:{x[0]}")
	print(f"姓名:{x[2]}")
只有直接執行 01時，以下程式才會跑
if _name_ =="_main_":
  name="我是靜宜大學 行銷數位四A 徐梓恩"
  split(name)