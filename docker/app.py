import sys
from flask import Flask
from flask import request

app = Flask(__name__)


def got_here():
    return('got here')


def post_to_stdout(request):
    if request.form:
            print('Form:' + str(request.form), file=sys.stderr)
    if request.data:
            print('Data:' + str(request.data), file=sys.stderr)

    return '' 

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return post_to_stdout(request)
    else:
        return got_here()

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port="80")
