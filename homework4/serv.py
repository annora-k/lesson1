from flask import Flask, render_tempate

my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
    return  render_tempate('index.html')


@my_flask_app.route('/all/')
def all_news():
    return  render_tempate('all_the_news.html')



if __name__ == "__main__":
    my_flask_app(debag=True)