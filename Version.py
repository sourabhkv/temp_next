import requests,re
content = requests.get("https://sourabhkv.github.io/ytdl/")
content.close()
all_num = (re.findall(r'\d\d\.\d\d\d\d\.\d\d',content.text))
print(all_num,type(all_num[0]))
z=[]
for i in range(len(all_num)):
    z.append(int((re.findall("\d+",all_num[i])[0])+(re.findall("\d+",all_num[i])[1])+(re.findall("\d+",all_num[i])[2])))

print(z)
