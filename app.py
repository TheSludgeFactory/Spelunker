from flask import Flask, request, render_template, url_for
from flask_bootstrap5 import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['DEBUG'] = True

@app.route('/')
def main():
    title = 'How To Reset The Root Password On Linux'
    author = 'H. P. Lovecraft'
    date = '2022.05.10'
    img_f = url_for('static',filename='/assets/images/python-logo-thumbnail.png')
   
    return render_template('index.html',t_title=title,a_name=author,d_date=date,img_f=img_f)

@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">
                  <input type="text" name="name">
                  <input type="text" name="location">
                  <input type="submit" value="Submit">
              </form>'''

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    s = '<h1>Hello {}. You are from {}. You have submitted the form successfully! \
    <h1><Form action="/theform"><input type="submit" value="Return"</button></form>'.format(name, location) 

    return '{}'.format(s)

if __name__ == '__main__':
    app.run()