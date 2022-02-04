from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
  date = datetime.datetime.now()
  if 'total_count' in session:
    session['account_total'] = 0
  return render_template("index.html", date=date)

@app.route('/process', methods=['POST'])
def process_transaction():
  if request.form['which_form'] == 'farm':
    session['account_total'] += random.randint(10,20)
  elif request.form['which_form'] == 'cave':
    session['account_total'] += random.randint(10,20)
  elif request.form['which_form'] == 'house':
    session['account_total'] += random.randint(10,20)
  elif request.form['which_form'] == 'casino':
    random_num = random.randint(1,2)
    if random_num == 1:
      session['account_total'] += random.randint(1,50)
    else:
      session['account_total'] += random.randint(-50,-1)
  else:
    print("NOT OKAY! OKAY!")
  return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

  # if session['activity']:
  #     session['activity'].append("<div class='color-red'><p>Sadge</p></div>")
  # else:
  #     session['activity'].append("<div class='color-red'><p>OkaygeBusiness</p></div>")