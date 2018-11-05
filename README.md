# README

Transfers style from one picture to another.
To <a href='http://www.vlfeat.org/matconvnet/pretrained/#downloading-the-pre-trained-models'> download the pretrianed vgg-19 model </a>

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

## How to use it
Firstly, install the dependencies </br>
<code>
  pip3 install -r requirements.txt
</code>
</br>
Then, in main.py 
</br>
Change these variables:
</br>
<ul>
  <li> path_model </li>
  <li> path_content </li>
  <li> path_style </li>
</ul>
</br>
To the path of it's corresponding file (pretrained vgg-19 model, content image and style image) </br>
And then </br>
<code>
  python3 main.py
</code>
</br>

