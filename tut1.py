from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    name="manan"
    return render_template('index.html',name2=name)

@app.route('/manan')
def hello_manan():
    return 'Hello manan kaise ho'

app.run(debug=True)

if __name__ == '__main__':
    app.run()