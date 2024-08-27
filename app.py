from flask import (
    Flask,
    render_template,
    redirect, url_for, 
    jsonify 
)
import requests

url = "https://leetcode.com/graphql"

questionData = {
	"total" : 0,
	"easy" : 0,
	"medium" : 0,
	"hard" : 0	
}

query = """
{
    matchedUser(username: "shiv09ds") {
        submitStats {
            acSubmissionNum {
                difficulty
                count
                submissions
            }
        }
    }
}
"""

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def fetchApi():
    response = requests.post(url, json={'query': query})
    data = response.json()
    
    if 'data' in data and 'matchedUser' in data['data'] and data['data']['matchedUser']:

        questionData["total"] = data['data']['matchedUser']['submitStats']['acSubmissionNum'][0]['count']
        questionData["easy"] = data['data']['matchedUser']['submitStats']['acSubmissionNum'][1]['count']
        questionData["medium"] = data['data']['matchedUser']['submitStats']['acSubmissionNum'][2]['count']
        questionData["hard"] = data['data']['matchedUser']['submitStats']['acSubmissionNum'][3]['count']
    
        return questionData
    else:
        print("not found or an error occurred.")

@app.route("/api/data")
def data():
    return jsonify(fetchApi())

if __name__ == "__main__":
    app.run(debug= True, port = 1234)