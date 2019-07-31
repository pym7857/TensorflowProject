from flask import Flask, render_template, request

import datetime
import tensorflow as tf
import numpy as np

app = Flask(__name__)

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([4, 1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

hypothesis = tf.matmul(X, W) + b

# 저장된 학습모델 불러오기 위한 초기화
saver = tf.train.Saver()
model = tf.global_variables_initializer()
sess = tf.Session()
sess.run(model)

save_path = "./model/saved.cpkt"
saver.restore(sess, save_path)      # 해당 세션에 저장된 학습모델을 불러온다.

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
      return render_template('index.html')
    if request.method == 'POST':
        avg_temp = float(request.form['avg_temp'])
        min_temp = float(request.form['min_temp'])
        max_temp = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])

    price = 0   # price 변수 생성

    data = ((avg_temp, min_temp, max_temp, rain_fall),)
    arr = np.array(data, dtype=np.float32)

    x_data = arr[0: 4]
    dict = sess.run(hypothesis, feed_dict={X: x_data})

    price = dict[0]
    return render_template('index.html', price=price)   # 서버로 price 변수값 보냄

if __name__ == '__main__':
    app.run(debug=True)