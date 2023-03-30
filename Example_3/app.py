from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    name = request.form['name']
    location = request.form['location']
    return f"你的名字是{name}，你的位置是{location}。"

if __name__ == '__main__':
    app.run(debug=True)


'''
上述代码可以使用普通的HTML表单提交来实现相同的功能。但是使用Ajax可以带来一些好处，如下：

无需重新加载整个页面：当使用普通的HTML表单提交时，整个页面都会被重新加载，这可能会导致页面闪烁和用户体验变差。而使用Ajax，只有表单数据被提交，页面的其余部分保持不变，用户不会看到任何页面刷新。

更快的响应时间：由于Ajax只提交表单数据，而不是整个页面，所以相对于传统的HTML表单提交，它可以更快地响应请求。这对于对性能有要求的应用程序（例如，实时的聊天应用程序）非常重要。

更好的用户体验：使用Ajax可以使应用程序更加流畅和响应，给用户带来更好的使用体验。例如，用户可能希望在填写表单时查看某些实时数据，而Ajax可以在不中断表单提交的情况下加载这些数据。

总之，使用Ajax可以提高应用程序的性能和用户体验，特别是对于需要实时响应和交互的应用程序来说非常重要。
'''
