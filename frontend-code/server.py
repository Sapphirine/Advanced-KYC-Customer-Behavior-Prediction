from flask import Flask, request, render_template, g, redirect, Response,url_for
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row, SQLContext
import pandas as pd
import glob
import docx
import json

app = Flask(__name__)

f = open("output.txt", "r")
li = json.loads(f.read())
f.close()
# print(li)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/result', methods = ['Get', 'Post'])
def result():
    customer_id = request.form['customer_id']
    price = request.form['Price']
    if customer_id in li:
        dis = int(li[customer_id])
        price = int(price)
        if dis >= 9:
            discount_num = price * 0.8
        elif dis >= 6:
            discount_num = price * 0.9
        else:
            discount_num = price
        return render_template("result.html", customer_id = customer_id, discount_num = discount_num)
    else:
        discount_num = price
        return render_template("result.html", customer_id = customer_id, discount_num = discount_num)

if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:
        python server.py
    Show the help text using:
        python server.py --help
    """

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()




