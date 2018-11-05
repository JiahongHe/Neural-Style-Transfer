from model import NST

if __name__ == '__main__':
    path_model = 'trained_model/imagenet-vgg-verydeep-19.mat'
    path_content = 'images/jh.jpg'
    path_style = 'images/van.jpg'
    num_iterations = 200

    NST(path_model, path_content, path_style, num_iterations)


