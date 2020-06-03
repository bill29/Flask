from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return 'hello world, %s' %name
@app.route('/goodbye/<name>')
def good_bye(name):
    return  'Goodbye ' + name
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog number %d' %postID
app.add_url_rule('/nguyenminhdan', 'hello', hello_world)
if __name__ == '__main__':
    app.run(debug=True)
