from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text1 = request.form['text1']  # 获取第一个文本框的内容
        text1 = '你竟然输入的是：' + text1
        return render_template('index.html', text2=text1)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    #app.run()
    app.run(port=8000)
    #app.run(host='0.0.0.0', port=8080)
