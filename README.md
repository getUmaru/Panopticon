# Panopticon

For anyone wanting to help please ingore everything except motionDetect/colormotion_detector

This is a repository that displays my openCV work in Python. It is called Panopticon as Panopticon is Foucalt's view on power through institutions. This also reflects Jeremny Benthams's view as he coined the term. It is meant to be ironic since this is a motion tracking system.


<h2>Installation</h2>
<ul>
  <li> install python3 from python website</li>
  <li> open cmd as adminstrator</li>
  <li> pip install numpy</li>
  <li> pip install matplotlib</li>
  <li> pip install opencv-python</li>
</ul>

<h2> Specifics </h3>

I have switched from using any prior language to using Python, even though it is a higher level language, I enjoy the simplicty and versatility of the language itself which allows for many things. The modules in python are also very cool as there are many

Anyways

This openCV stuff I have been working on has mainly been for a school science fair. The main purpose of the project is to build a train system that is completely propelled and levitated by electromagnetic fields. We are using solenoids for propulsion and ferrous magnets for levitation

The part whre the software is being introduced is in <b>two parts:</b>

<h3>I: OpenCV</h3>

OpenCV in this case is to act as a security measure against any train derailments. Within openCV I will track the motion of the train, here after referred to as a payload, such that if it leaves a certain area it will trigger emergency services or technical services. I also had to ensure that other objects within the motion capture field system would not interfere with the train motion itself. My solution to this issue was using a color segmentation motion tracking system. This way other objects outside the system will not interfere with the payload so long as it is not the same color

I began this process by distinguishing colors in still images. The results were satisfying, as displayed below.

<img src="https://i.imgur.com/GnAYrJK.jpg"/> <img src="https://i.imgur.com/to0BcJF.jpg"/> 

The image below is using my webcam to track actual color objects based on a color range I set
<img src="https://i.imgur.com/Af0XpqQ.jpg"/>

<h3>II: Arduino </h3>

You wont see much arduino stuff since I am not well versed in that area. Hopefully I will start to learn soon. 
