from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ =='__main__':
    app.run()

# 运行后，打开所给的即可。
