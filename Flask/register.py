from flask import Flask , render_template , request
web = Flask(__name__)

@web.route('/')
@web.route('/register')
def register():
    return render_template('register.html')

@web.route('/register_confirm', methods = ['POST'])
def register_confirm():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        return render_template('register_confirm.html',first_name = first_name, last_name = last_name, email = email, phone = phone)



@web.route('/login')
def home():
    return "Hello Worlds"


if __name__ == '__main__':
    web.run(debug=True)


