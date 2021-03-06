from flask import Flask, jsonify, request
  
app = Flask(__name__)
@app.route("/")
def home_view():
        return "<h1>Once upon a time at MISIS!</h1>"
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
@app.route("/sample_search")
def search_question2():
        question = {"count":10,"response":[["\u0413\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430 \u2014 \u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f","https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%83%D0%B7%D0%B0","https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Right_triangle_with_notations.svg/1200px-Right_triangle_with_notations.svg.png"],["\u0433\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430 - Translation into English - examples Russian | Reverso ...","https://context.reverso.net/translation/russian-english/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%83%D0%B7%D0%B0","NULL"],["\u0433\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430 - Wiktionary","https://en.wiktionary.org/wiki/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%83%D0%B7%D0%B0","NULL"],["\u0413\u0418\u041f\u041e\u0422\u0415\u041d\u0423\u0417\u0410 - Translation in English - bab.la","https://en.bab.la/dictionary/russian-english/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%83%D0%B7%D0%B0","NULL"],["\u0433\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430 \u2014 \u0412\u0438\u043a\u0438\u0441\u043b\u043e\u0432\u0430\u0440\u044c","https://ru.wiktionary.org/wiki/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%83%D0%B7%D0%B0","https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Triangle_with_notations.svg/1200px-Triangle_with_notations.svg.png"],["\u0433\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430 in Armenian - Russian-Armenian Dictionary | Glosbe","https://glosbe.com/ru/hy/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%83%D0%B7%D0%B0","NULL"],["\u0413\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430, \u043f\u0440\u0438\u043b\u0435\u0436\u0430\u0449\u0438\u0439 \u0438 \u043f\u0440\u043e\u0442\u0438\u0432\u043e\u043b\u0435\u0436\u0430\u0449\u0438\u0439 \u043a\u0430\u0442\u0435\u0442\u044b (\u0441\u0442\u0430\u0442\u044c\u044f ...","https://ru.khanacademy.org/math/trigonometry/trigonometry-right-triangles/xfefa5515:ratios-in-right-triangles/a/opposite-adjacent-hypotenuse","https://lh3.googleusercontent.com/K5bzbA067FpSFjs7VuTCAEosuCGLm4NfxQbq_tYtpMHIyB5j-nirP_Pdy8XXrmoARE3_2TBnGafYaRTsSiFt4iw"],["\u041f\u0440\u043e\u0438\u0441\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0441\u043b\u043e\u0432\u0430 \u0433\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430. \u042d\u0442\u0438\u043c\u043e\u043b\u043e\u0433\u0438\u044f \u0441\u043b\u043e\u0432\u0430 \u0433\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430","https://lexicography.online/etymology/%D0%B3/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%83%D0%B7%D0%B0","https://s.lexicography.online/images/og3.png"],["\u0413\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430 \u0432 \u043f\u0440\u044f\u043c\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u043e\u043c \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u0435 - \u0444\u043e\u0440\u043c\u0443\u043b\u0430, \u043f\u0440\u0438\u043c\u0435\u0440 ...","https://2mb.ru/matematika/geometriya/gipotenuza-v-pryamougolnom-treugolnike/","NULL"],["\u0413\u0418\u041f\u041e\u0422\u0415\u041d\u0423\u0417\u0410 - \u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 - bab.la","https://www.babla.ru/%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9/%D0%B3%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%83%D0%B7%D0%B0","NULL"]]}
        return jsonify(response = question)
