# Importing
from flask import Flask , render_template
import os

# Interaction
app = Flask(__name__)

pic_folder = os.path.join('static')

app.config['UPLOAD_FOLDER'] = pic_folder
# Mapping
@app.route('/')
# Inputs
def index():
    pic = os.path.join(app.config['UPLOAD_FOLDER'],'demo.jpg')
    return render_template('home.html',user_image=pic)

@app.route('/about')
def about():
    return  "Welcome to the About page"
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/indexhome')
def index_home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)