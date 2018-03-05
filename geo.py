

import json

fname = 'dat.json'
i = 0
with open(fname, 'r') as f:
	geo_data = {
		"type": "FeatureCollection",
		"features": []
	}
	for line in f:
	#	print("1")
		tweet = json.loads(line)
		#print(json.dumps(tweet, indent=4))
		t = f.readline()
		
		if tweet['coordinates']:
			print(i)
			i = i +1
			geo_json_feature = {
				"type": "Feature",
				"geometry": tweet['coordinates'],
				"properties": {
					"text": tweet['text'],
					"created_at": tweet['created_at']
				}
			}
			print(geo_data['feature'])
			geo_data['features'].append(geo_json_feature)


with open('geo_data.json', 'w') as fout:
	fout.write(json.dumps(geo_data, indent=4))