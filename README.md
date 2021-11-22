<!-- image -->
<div align="center" id="top"> 
  <img src=images/ex1.png width="500" />
  &#xa0;
</div>

<h1 align="center"> bilateration-mobile-robot-localization </h1>
<h2 align="center"> Mobile robot localization using simple bilateration method </h2>

<!-- https://shields.io/ -->
<p align="center">
  <img alt="Top language" src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python">
  <img alt="Status" src="https://img.shields.io/badge/Status-done-green?style=for-the-badge">
</p>

<!-- table of contents -->
<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#package-content">Content</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#eyes-implementation">Implementation</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="#technologist-author">Author</a> &#xa0; | &#xa0;
</p>

<br>


## :dart: About ##
Bi-lateration method used two reference points and distances between those points and a robot to determine the position of the robot. It uses the least square method to minimise the error between distances read from scanner and assumed coordinates. Bi-lateration is a subtype of the multi-lateration method, limited to only two points.

<div align="center" id="put_id"> 
  <img src=images/dist.png width="150" />
  &#xa0;
</div>

## :package: Content
 * [bilateration.py](bilateration.py) - main script
 * [fwd.json](data/fwd.json) - file with example data


## :checkered_flag: Starting ##
```bash
# Clone this project
$ git clone https://github.com/KamilGos/bilateration-mobile-robot-localization

# Access
$ cd bilateration-mobile-robot-localization

# Run the project
$ sudo python3 bilateration.py
```

## :memo: License ##

This project is under license from MIT.

## :technologist: Author ##

Made with :heart: by <a href="https://github.com/KamilGos" target="_blank">Kamil Goś</a>

&#xa0;

<a href="#top">Back to top</a>



<!-- ADDONS -->
<!-- images -->
<!-- <h2 align="left">1. Mechanics </h2>
<div align="center" id="inventor"> 
  <img src=images/model_1.png width="230" />
  <img src=images/model_2.png width="236" />
  <img src=images/model_3.png width="228" />
  &#xa0;
</div> -->

<!-- one image -->
<!-- <h2 align="left">2. Electronics </h1>
<div align="center" id="electronics"> 
  <img src=images/electronics.png width="500" />
  &#xa0;
</div> -->


<!-- project dockerized -->
<!-- <div align="center" id="status"> 
  <img src="https://www.docker.com/sites/default/files/d8/styles/role_icon/public/2019-07/Moby-logo.png" alt="simulator" width="75" style="transform: scaleX(-1);"/>
   <font size="6"> Project dockerized</font> 
  <img src="https://www.docker.com/sites/default/files/d8/styles/role_icon/public/2019-07/Moby-logo.png" alt="simulator" width="75"/>
  &#xa0;
</div>
<h1 align="center"> </h1> -->