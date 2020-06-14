from flask import Flask, render_template, request, redirect, jsonify, make_response
from Extract import extract
from TextSummariser import text_rank

app = Flask(__name__)


@app.route("/api", methods=['POST'])
def summariser():

    reqData = request.get_json()
    print(reqData)
    res = extract(reqData["url"])

    data = res["content"]
    t = res["title"]
    title = t[0].text

    summary = text_rank(data)

    res = make_response(jsonify(
        {"Summary": summary, "Title": str(title)}), 200)

    return res


if __name__ == '__main__':
    app.run(debug=True)
