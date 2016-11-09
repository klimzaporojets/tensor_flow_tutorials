# an example on how fetches work 
# To fetch the outputs of operations, execute the graph with a run() call on 
# the Session object and pass in the tensors to retrieve. 
# You can also fetch multiple tensors
import tensorflow as tf 

input1 = tf.constant([3.0])
input2 = tf.constant([2.0])
input3 = tf.constant([5.0])
intermed = tf.add(input2, input3)
mul = tf.mul(input1, intermed)

with tf.Session() as sess:
  result = sess.run([mul, intermed])
  print("Result of fetches: {}".format(result))
