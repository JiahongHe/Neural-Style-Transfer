from model import NST

if __name__ == '__main__':
    path_model = 'trained_model/imagenet-vgg-verydeep-19.mat'
    path_content = 'images/original.jpg'
    path_style = 'images/mona.jpg'
    num_iterations = 4000
    alpha = 400
    beta = 10
    start_from_content = True

    NST(path_model, path_content, path_style, num_iterations, alpha, beta, start_from_content)

