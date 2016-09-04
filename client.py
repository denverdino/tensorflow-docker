import tensorflow as tf
import numpy as np

train_X = np.linspace(-1, 1, 101)
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.33 + 10

X = tf.placeholder("float")
Y = tf.placeholder("float")
w = tf.Variable(0.0, name="weight")
b = tf.Variable(0.0, name="reminder")

init_op = tf.initialize_all_variables()
cost_op = tf.square(Y - tf.mul(X, w) - b)
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost_op)

with tf.Session("grpc://localhost:8080") as sess:
    with tf.device("/job:worker/task:0"):
        sess.run(init_op)
        for i in range(10):
            for (x, y) in zip(train_X, train_Y):
                sess.run(train_op, feed_dict={X: x, Y: y})
        
        print(sess.run(w))
        print(sess.run(b))
