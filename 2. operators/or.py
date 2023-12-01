docs = [
	"new home sales top forcasts",
	"home sales rise in july",
	"increase in home sales in july"
]
query = "new OR increase"
#############################################################
dic = {}
for i, doc in enumerate(docs):
	for word in doc.split(" "):
		if word not in dic: dic[word] = []
		dic[word] += [ i ] 
res = []
for q in query.split(" OR "):
	res += dic[q]
res = set(res)
#############################################################
print(dic)
print("Result:", res)
#############################################################
