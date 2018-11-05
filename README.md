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

## How to use it
<code>
  pip3 install -r requirements.txt
</code>
Then, in main.py </br>
Change these variables:
<ul>
  <li> path_model </li>
  <li> path_content </li>
  <li> path_style </li>
</ul>
To the path of it's corresponding file (pretrained vgg-19 model, content image and style image) </br>
And then </br>
<code>
  python3 main.py
</code>

