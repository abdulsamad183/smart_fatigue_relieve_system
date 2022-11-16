# smart_fatigue_relieve_system
It detects the human condition whether he/she is tired or not tired. Based on human condition ,electrical appliances will control and do some necessary things to get relief from tiredness.

# Scope for Innovtion
We propose a fully automated Smart System which is independent of manual intervention. It Automatically detects human condition by image processing and control the electrical appliances so that we save power by turning ON only when human requires and relieve from fatigue automatically. 

# Main principle behind this .
Using Computer vision algorithms we detect facial condition of humans . Based on results micro controller will do necessary actions like controlling AC and other electrical appliances to relieve tiredness

![Block Diagram](https://github.com/[abdulsamad183]/[smart_fatigue_relieve_system]/blob/[master]/block_diagram.jpg?raw=true)

# How this works ( What are those files ? )
## yolo_detect.py
It is a python script which predicts only  whether human is tired or not tired. It is for only detection of human . 

## original.py
It is a python script in which Whole process is present in this script. It detects the human condition .Based on human condition , If human is not tired , simply it will print " You are Not Tired. " If human is tired , two motors will turn ON (in real life assume it as AC,FAN), Pleasant Songs will be played , Some relaxation tips will be given and A mini vehicle which consists of glass of water will move forward and move backward after completion of drinking of water (here mini vehicle can be assumed that we can relate this for IoT Applications).

## TechFest.ino 
It is a arduino file which it will controls hardware i.e., it controls DC Motors , Servo Motors , IR Sensor.

## yolov3_custom.cfg
It is a configured custom yolo configuration file . It is used to store information regarding configuration and settings for computer programs.

## yolov3_custom_4000.weights.txt
Trained weights . There is google drive link to download the trained weights.

## Songs.zip 
It is a folder consists of songs (mp3 format) to play while human is tired.
