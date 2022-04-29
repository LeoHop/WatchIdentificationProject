# Luxury Watch Identification - An AI Program for Avid Horologists

## What is Luxury Watch Identification? 
This program's intention was to take an image URL from the internet and detect A) If a watch is present in the image and B) What the brand of the luxury watch is.
This is intended to be utilized by people interested in identifying certain watches they see on the internet. From amateur watch enthusiasts to advanced Horologists, this programed is designed to be of use to any audience!

## How Does Luxury Watch Identification work?
By utilizing two forms of Artificial Intelligence APIs, Google Cloud Vision Image Recognition and Clarifai's Apparel Detection Model, this Luxury Watch Identification program can automatically detect certain qualities / concepts of images.

Once certain concepts have been identified by the APIs, python is utilized to sort through the concepts to identify the main ideas such as whether or not there is a watch present in the image as well as the brand of the watch presented in the image. 
## Getting Started
Before continuing, make sure you have an API key for Clarifai and Google cloud vision. When using this program, you must include these json files within your project folder allowing for the python code to reference them. You can acquire the proper keys [here](https://github.com/LeoHop/WatchIdentificationProject).

### Setting Up Luxury Watch Identification to Run
Once you have included the necessary API keys using the Json files, you also must import the python file as well as the `requirements.txt` file into PyCharm. In PyCharm, the next step will be to go into terminal where you would then run the following command to import the necessary python packages. 

Run this command:   pip install -r requirements.txt

### Applying Google Credentials

The last step for setting up the program to run successfully is to go into your configurations in PyCharm and add the following command to your Envionrmal Variable section of the configurations.

Add this command following the PYTHONUNBUFFERED=1 in your environmental variable:

GOOGLE_APPLICATION_CREDENTIALS= (path of `cred.json` on your computer)

## Run the Program!
To run the program, double check you have completed all of the steps:

You have:
- Downloaded the python file of Main.py which you can find [here](https://github.com/LeoHop/WatchIdentificationProject)
- Downloaded all of the necessary python packages using the requirements.txt file 
- Added the necessary Json API keys
- Added the Google Cloud Credentials to your environmental variables.

Once all the steps above are complete, the last step is to click run. Then, all you have to do is find an image online, right click on the image, and click on "copy image address". Once this is copied all you have to do is paste it into the input once the program is running.

The best possible images are listed at the top of the python file. These image URLs will exemplify the capabilities of this program.
 

## *Created for Latin School of Chicago's Algorithms Class*
 \
![algorithms and data structures](/assets/header.jpeg)
 
 
