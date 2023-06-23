from flask import Flask, render_template, request
from recommend import Recommend

app = Flask(__name__)

@app.route('/')
def title():
    return render_template('title.html')

@app.route('/step1', methods=['GET', 'POST'])
def era_1():
    global a_1
    if request.method == 'GET':
        return render_template('era_1.html')
    if request.method == 'POST':
        a_1 = request.form['form']
        return render_template('era_1.html', a_1=a_1)

@app.route('/step2', methods=['GET', 'POST'])
def era_2():
    if request.method == 'GET':
        return render_template('era_2.html')
    if request.method == 'POST':
        a_2 = request.form['form']
        recommend.era_choice(a_1, a_2)
        return render_template('era_2.html', a_2=a_2)

@app.route('/step3', methods=['GET', 'POST'])
def acter_3():
    if request.method == 'GET':
        return render_template('acter_3.html')
    if request.method == 'POST':
        a_3 = request.form['form']
        recommend.acter1_choice(a_3)
        return render_template('acter_3.html', a_3=a_3)

@app.route('/step4', methods=['GET', 'POST'])
def acter_4():
    if request.method == 'GET':
        return render_template('acter_4.html')
    if request.method == 'POST':
        a_4 = request.form['form']
        recommend.acter2_choice(a_4)
        return render_template('acter_4.html', a_4=a_4)

@app.route('/step5', methods=['GET', 'POST'])
def acter_5():
    if request.method == 'GET':
        return render_template('acter_5.html')
    if request.method == 'POST':
        a_5 = request.form['form']
        recommend.acter3_choice(a_5)
        return render_template('acter_5.html', a_5=a_5)
    
@app.route('/step6', methods=['GET', 'POST'])
def writer_6():
    if request.method == 'GET':
        return render_template('writer_6.html')
    if request.method == 'POST':
        a_6 = request.form['form']
        recommend.writer_choice(a_6)
        return render_template('writer_6.html', a_6=a_6)

@app.route('/result', methods=['GET', 'POST'])
def result():
    final_result = recommend.result()
    return render_template('result.html', final_result = final_result)

if __name__ == "__main__":
    recommend = Recommend()
    app.run(debug=True)