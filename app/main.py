from flask import Flask, jsonify, request
  
app = Flask(__name__)
@app.route("/"):
def home():
        return "<H1>Once upon a time at MISIS!</H1>"
@app.route("/search")
def search_question():
        question = request.args.get('question')
        import googleapiclient.discovery as gc
        service = gc.build("customsearch", "v1", developerKey= "AIzaSyC3EeNpQWJKlNrsLWY2BeERN7lsCK55VyE")
        res = service.cse().list(q = question,cx = '8fa0dc9f3a0a72baa').execute()
        links = []
        for iter in range(10):
        links.append([res['items'][iter]['title'], res['items'][iter]['link'],
                        res['items'][iter]['pagemap']['cse_image'][0]['src']
                        if 'cse_image' in res['items'][iter]['pagemap'].keys() else 'NULL'])
        return jsonify(count = 10, response = sites)
