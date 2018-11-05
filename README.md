# README

Transfers style from one picture to another.

Original image </br>
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
In main.py 
</br>
Change these variables: </br>
<code> path_model </code> </br>
<code> path_content </code> </br>
<code> path_style </code> </br>

To the path of it's corresponding file (pretrained vgg-19 model, content image and style image) </br>
And then </br>
<code>
  python3 main.py
</code>
</br>

## Hyperparameters

variable

