from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Security: enables Flash messaging

feedbacks = []

@app.route('/')
def home():
    return render_template('home.html', feedbacks=feedbacks)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']
        if not name or not feedback:
            flash('All fields are required!')
            return redirect(url_for('feedback'))
        feedbacks.append({'name': name, 'feedback': feedback})
        flash('Feedback submitted!')
        return redirect(url_for('home'))
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
