from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Saraiya Rogers! This is my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    message = f"You entered your favorite course as: {subject} {course_number}"
    favorite_courses = ['BMGT301', 'BMGT302', 'BMGT303', 'BMGT304', 'BMGT305']
    return render_template('favorite-course.html', message=message, courses=favorite_courses)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        comment = request.form['comment']
        return render_template('contact.html', thank_you=True, first_name=first_name, last_name=last_name, email=email, comment=comment)
    return render_template('contact.html', thank_you=False)

if __name__ == '__main__':
    app.run(debug=True)
