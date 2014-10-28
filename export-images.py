import urllib, json, os, sys

oid = sys.argv[1]

url = "http://app.ecwid.com/api/v1/" + oid+ "/products"
data = json.loads(urllib.urlopen(url).read())

images = dict((x['id'], x.get('originalImageUrl', None)) for x in data)

if not os.path.exists(oid):
	os.makedirs(oid)

for k in images.keys():
	if images[k] != None:
		print "Start downloading" ,images[k]
		urllib.urlretrieve(images[k], oid + "/" + str(k) + ".jpg")
		print "Finish downloading" ,images[k]
