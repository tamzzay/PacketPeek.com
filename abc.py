from flask import Flask, render_template
app = Flask(__name__)


def run_my_program():
    pass


@app.route('/login')
def login():
    output = run_my_program() # This function should generate the desired output of your Python program
    return render_template('login.html', output=output)
if __name__ == '__main__':
    app.run()

