import tensorflow as tf
import numpy as np

X = tf.placeholder(tf.float32, shape=[None, 4])     # 4개의 변인이 들어갈 공간 생성 (shape = 배열)
Y = tf.placeholder(tf.float32, shape=[None, 1])     # 1개의 변인이 들어갈 공간 생성
W = tf.Variable(tf.random_normal([4, 1]), name="weight")    # 4x1 행렬로 W 변수 난수 생성
b = tf.Variable(tf.random_normal([1]), name="bias")         # 1x1 행렬로 b 변수 난수 생성

hypothesis = tf.matmul(X, W) + b

# 저장된 학습모델 불러오기 위한 초기화
saver = tf.train.Saver()                    # 저장 객체 초기화
model = tf.global_variables_initializer()   # 모델 초기화

# 사용자 입력
avg_temp = float(input('평균 온도: '))
min_temp = float(input('최저 온도: '))
max_temp = float(input('최고 온도: '))
rain_fall = float(input('강수량: '))

with tf.Session() as sess:
    sess.run(model)

    save_path = "./saved.cpkt"          # 저장된 학습 모델 경로
    saver.restore(sess, save_path)      # 해당 세션에 저장된 학습모델을 불러온다.

    data = ((avg_temp, min_temp, max_temp, rain_fall), )    # 2차원 배열 (원본 데이터도 2차원 배열이기 때문)
    arr = np.array(data, dtype=np.float32)                  # 입력한 데이터로 만든 arr 배열
    print(arr)
    x_data = arr[0: 4]

    dict = sess.run(hypothesis, feed_dict={X: x_data})
    print(dict[0])