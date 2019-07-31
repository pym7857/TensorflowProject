import tensorflow as tf
import numpy as np
from pandas.io.parsers import read_csv

model = tf.global_variables_initializer()

data = read_csv('price data.csv', sep=',')  # 토큰 = ','

xy = np.array(data, dtype=np.float32)       # xy 변수에 2차원 배열 행렬 형태로 해당 데이터를 담는다.
print(xy)

# 2차원배열 슬라이싱 => xy[행, 열]
x_data = xy[:, 1:-1]    # 첫번째 ~ 네번째 열
y_data = xy[:, [-1]]    # 마지막 열

X = tf.placeholder(tf.float32, shape=[None, 4])     # 4개의 변인이 들어갈 공간 생성 (shape = 배열)
Y = tf.placeholder(tf.float32, shape=[None, 1])     # 1개의 변인이 들어갈 공간 생성
W = tf.Variable(tf.random_normal([4, 1]), name="weight")    # 4x1 행렬로 W 변수 난수 생성
b = tf.Variable(tf.random_normal([1]), name="bias")         # 1x1 행렬로 b 변수 난수 생성

hypothesis = tf.matmul(X, W) + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))    # 비용: (예측값 - 실제값)^2 의 평균값
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())     # 초기화

for step in range(10001):
    cost_, hypo_, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 500 == 0:
        print("[ #", step, "] (손실)비용: ", cost_)
        print("배추(예측)가격: ", hypo_[0])

# 학습 모델 저장
saver = tf.train.Saver()
save_path = saver.save(sess, "./saved.cpkt")
print("학습된 모델을 저장했습니다.")             # checkPoint 형태로 저장됨