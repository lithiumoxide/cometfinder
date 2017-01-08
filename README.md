# cometfinder
## About
This code allows for easy searching for comets in SOHO images, without the need for blinking images or otherwise preparing images before analysing. It's based on the tutorial at https://www.linuxvoice.com/comet-python/. This code is neither efficient nor good, but helps make finding comets easier. It runs with Python 2.7.
## Usage
Before running, make sure you install the following packages:

    sudo apt-get install python-numpy python-scipy python-matplotlib python-tk

Go to https://sohodata.nascom.nasa.gov/cgi-bin/data_query and search for LASCO C2 or LASCO C3 images (1024 pixels). Download four sequential images (they're taken 12 minutes apart.

In **cometfinder.py** set the location of the images in the image1, image2, image3, and image4 lines, near the start of the file.

The variable **thold** sets the exclusion threshold: the higher the number the cleaner the images will be, but fainter objects will be removed from the images.

The variables **x1**, **x2**, **y1**, **y2** set the coordinates for a rectangle in the image. This rectangle can be set to approximately where you expect comets to appear (see below).

To run, simply use:

    python cometfinder.py

When run, a visual plot of the images will open up, displaying differences between each image in blue and red. There will be a lot of noise in the images. Planets and stars will appear as horizontal rows of four points (blue-red-blue-red), whereas comets will appear as diagonal sequences of four points.
## Further information and reporting comets
Info on comet-hunting can be found at https://sungrazer.nrl.navy.mil/. This site also has details on where comets can be found in the images (its dependent on the time of year, due to the orbiting nature of the SOHO spacecraft.

This website also allows you to report comets you have found. Please do read all the information first before reporting a suspected comet.
