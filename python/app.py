from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'message': '🙂 success !!!',
        'data': data
    }),200

# ----- class 137 ------

# @app.route('/planet')
# def planet():
#     name = request.args.get('name')
#     return name
    # planet_data = next(item for item in data if item["name"] == name)
    # return jsonify({
    #         'message': '🙂 success !!!',
    #         'data': planet_data
    #     }),200

# xxxxxx class 137 xxxxxx


if __name__ == '__main__':
    app.run()
