from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return render_template('homepage.html', name)


@app.route('/index/<name>')
def index(name):
   return render_template('homepage.html', name=name)
@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      data = request.form
      user_name = data['username']
      pass_word = data['password']
      if user_name == 'minhdan' and pass_word == '123':
         return 'welcome'
      else:
         return 'fail'
@app.route('/signin')
def sign_in():
   return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)