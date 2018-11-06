# README

Transfers style from one picture to another. </br>
To know how nerual style transfer works: </br>
<a href='https://www.youtube.com/watch?v=Re2C9INXCNc&index=38&list=PLBAGcD3siRDjBU8sKRk0zX9pMz9qeVxud'> Andew Ng's course </a> </br>
<a href='https://arxiv.org/abs/1508.06576'> Original paper </a> </br>

## Original image 
<img src='pics/original.jpg'> 

## Style: Van Gogh
Style image </br>
<img src='pics/van.jpg'> </br>
Generated image </br>
<img src='pics/generated_van.jpg'>

## Style: Leonardo da Vinci
Style image </br>
<img src='pics/mona.jpg'> </br>
Generated image </br>
<img src='pics/generated_mona.jpg'>

## Usage
Firstly, install the dependencies </br>
<code>
  pip3 install -r requirements.txt
</code>
</br>
Then download the pretrianed vgg-19 model. </br>
Search <code>imagenet-vgg-verydeep-19</code> in <a href='http://www.vlfeat.org/matconvnet/pretrained/#downloading-the-pre-trained-models'>this page</a> and download <code>imagenet-vgg-verydeep-19.mat</code>.</br> 
In <code>main.py</code>, Change these variables: </br>
<code> path_model </code> </br>
<code> path_content </code> </br>
<code> path_style </code> </br>

To the path of it's corresponding file (pretrained vgg-19 model, content image and style image), And then </br>
<code>
  python3 main.py
</code>
</br>

## Hyperparameters
Variables <code> alpha </code> and <code> beta </code> in <code> main.py </code> can be tuned to generate different results. </br>
The results above are generated with <code> alpha = 2000 </code> and <code> beta = 10 </code> </br>
In short words, <code> alpha </code> and <code> beta </code> determines the content loss's and style loss's contribution to the total loss. </br>
The generated image would be have more similar content to the content image with higher <code> alpha </code>, </br>
while the generated image would be more similar to the style image with higher <code> beta </code>. </br>

## Reference
Most of the code of this project come from the programming assignment of Coursera course <code> Convolutional Neural Networks </code> by Andew Ng. </br>
<a href='https://github.com/JiahongHe/Coursera-DeepLearning/blob/master/4%20Convolutional%20Neural%20Networks/week4/Art%2BGeneration%2Bwith%2BNeural%2BStyle%2BTransfer%2B-%2Bv2.ipynb'> The assignment notebook.</a>
