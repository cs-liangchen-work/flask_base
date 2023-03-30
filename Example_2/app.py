from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash, jsonify

app = Flask(__name__)

'''
@app.route('/')
def home():
    return render_template('home.html')
'''

@app.route('/searchOrg/', methods=['GET'])
def search():
    # /searchOrgNews?start=300&num=50
    print('----')
    start = int(request.args.get('start'))
    num = int(request.args.get('num'))
    result = {'start': start, 'num': num}
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    
'''
运行后的结果：
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://XXX.XX.XX.XXX:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 
'''
