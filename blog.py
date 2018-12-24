from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Show all restaurants
@app.route('/')
@app.route('/Tiv/')
def showBlog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
