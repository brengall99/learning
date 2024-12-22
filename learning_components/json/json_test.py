import json

mydict = {
	"people": [
		{	
		    "name": "Bob",
			"age": 28,
            "weight": 80
        },
        {
            "name": "Anna",
            "age": 34,
            "weight": 67
        },
        {	
		    "name": "Charles",
			"age": 45,
            "weight": 78
        },
        {
            "name": "Daniel",
            "age": 45,
            "weight": 110
        }
    ]
}

json_string = json.dumps(mydict, indent=4)
with open('/Users/brendangallagher/Desktop/learning/learning_components/json/mydata.json', 'w') as f:
    f.write(json_string)