from func_utils import *
import tensorflow as tf

STYLE_LAYERS = [
    ('conv1_1', 0.2),
    ('conv2_1', 0.2),
    ('conv3_1', 0.2),
    ('conv4_1', 0.2),
    ('conv5_1', 0.2)]

def NST(path_model, path_content, path_style, num_iterations):
    g = tf.Graph()
    with tf.Session(graph=g) as sess:

        model = load_vgg_model(path_model)
        content, style = get_img(path_content, path_style)
        generated = generate_noise_image(content)

        sess.run(model['input'].assign(content))
        out = model['conv4_2']
        a_C = sess.run(out)
        a_G = out
        J_content = compute_content_cost(a_C, a_G)

        sess.run(model['input'].assign(style))
        J_style = compute_style_cost(sess, model, STYLE_LAYERS)

        J = total_cost(J_content, J_style, alpha=10, beta=40)
        optimizer = tf.train.AdamOptimizer(2.0).minimize(J)

        sess.run(model['input'].assign(generated))
        #writer = tf.summary.FileWriter("tensorboard/", sess.graph)

    with tf.Session(graph=g) as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(num_iterations):
            sess.run(optimizer)
            generated = sess.run(model['input'])

            if i % 20 == 0:
                Jt, Jc, Js = sess.run([J, J_content, J_style])
                print("Iteration " + str(i) + " :")
                print("total cost = " + str(Jt))
                print("content cost = " + str(Jc))
                print("style cost = " + str(Js))
                save_image("images/" + str(i) + ".png", generated)

        save_image('images/generated_image.jpg', generated)
        sess.close()
    return
