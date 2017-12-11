from flask import Flask, render_template, request
from datetime import datetime

from algo import algorithm, algo_dict, not_learnt

app = Flask(__name__)


@app.route('/')
def index():
    st = datetime.now()
    print("\n\n\n---------------------------------\nindex started at {}".format(st))
    print("rendering the index page")
    Weekday_name = datetime.today().strftime('%A')
    algo = """no_algo_selected"""
    res = not_learnt
    score = """No_score"""
    print("serving empty result_")
    msg = """please sellect algorithm: DT, LR, RF, KNN, NB"""
    et = datetime.now()
    tt = et - st
    print("index process done in {}\n---------------------------------".format(tt))
    return render_template('script.html', week_day = Weekday_name, time=tt, msg=msg, algo=algo, res = res, score = score)


@app.route('/', methods=['POST', 'GET'])
def task():
    st = datetime.now()
    print('\n\n\n---------------------------------\nplease provide algo key')
    try:
        t = datetime.now()
        print("\ntask started at {}".format(t))
        Weekday_name = datetime.today().strftime('%A')
        algo = request.form['algo']
        print('using: {}'.format(algo))
        res, score = algorithm(algo) 
        print("serving algorithm result")
        msg = """your prediction is ready"""
        et = datetime.now()
        tt = et - st
        print("task executed successfully in {}".format(tt))
        return render_template('script.html', week_day = Weekday_name, time=tt, msg=msg, algo=algo, res = res, score = score)
    except ValueError as ve:
        t = datetime.now()
        print("\nexception caught at {}".format(t))
        Weekday_name = datetime.today().strftime('%A')
        algo = """Algo not learnt"""
        print("Incorrect found by me : {}".format(ve))
        print('error using: {}'.format(algo))
        res, score = algorithm(algo)
        msg = """Please check all the fields"""
        et = datetime.now()
        tt = et - st
        print("exception processed in {}\n---------------------------------".format(tt))
        return render_template('script.html', week_day = Weekday_name, time=tt, msg=msg, algo=algo, res = res, score = score)

if __name__ == '__main__':
    app.run(debug=True)