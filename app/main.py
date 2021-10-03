from flask import Flask, jsonify, request
  
app = Flask(__name__)
@app.route("/")
def home_view():
        return "<h1>Once upon a time in MISIS!</h1>"
@app.route("/search")
def search_question():
        theme = request.args.get('theme')
        body = request.args.get('body')
        question= theme +body
        import googleapiclient.discovery as gc
        print(question)
        service = gc.build("customsearch", "v1", developerKey= "AIzaSyBlY0nUDD-CzXBQHaqak2wONcsiovC-32M")
        res = service.cse().list(q = question, cx = '40707204fc194f9de').execute()
        res_img = service.cse().list(q = question,cx = 'c72347386ef0a3e86').execute()  
        res_vid = service.cse().list(q = question,cx = 'f229f9677b949d50b').execute()
        links = []
        vids = []
        pics = []
        for iter in range(len(res['items'])):
                links.append([res['items'][iter]['title'], res['items'][iter]['link'],res['items'][iter]['pagemap']['cse_image'][0]['src'] if 'cse_image' in res['items'][iter]['pagemap'].keys() else 'NULL'])
        for iter in range(len(res_vid['items'])):
                vids.append([res_vid['items'][iter]['title'], res_vid['items'][iter]['link'],res_vid['items'][iter]['pagemap']['cse_image'][0]['src'] if 'cse_image' in res_vid['items'][iter]['pagemap'].keys() else 'NULL'])
        for iter in range(len(res_img['items'])):
                pics.append([res_img['items'][iter]['title'], res_img['items'][iter]['link'],res_img['items'][iter]['pagemap']['cse_image'][0]['src'] if 'cse_image' in res_img['items'][iter]['pagemap'].keys() else 'NULL'])
        return jsonify(count = 10, sites = links, pics = pics, vids= vids)
