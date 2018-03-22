from flask import Flask, jsonify, request, render_template
import codecs 

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    comments = request.json['comment']
    results = []
    print comments[0].encode('utf-8')
    for res in comments:
        print res.encode("utf-8")
        results.append(res)
    print results[0]
    file = codecs.open("test.txt", "w", "utf-8")
    file.write(results[0])
    file.close()
    
    return jsonify(results)

@app.route("/index", methods=['GET'])
def main():
    return render_template('test.html')

@app.route("/policy", methods=['GET'])
def main():
    return render_template('policy.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)