# Arduino controlled fan




An app that turns on a 12v pc fan

it uses an arduino connected to my conputer and a relay to turn off and on a 60mm fan when the temperature reaches a certain point



### How to run:
To run and for developmentyou need python 3.11 or above[^1] and the arduino IDE

The physical materials are a 12v fan, an arduino, a relay and a power source for the fan

in terminal, navigate to the repository folder and run 

`python -m pip install -r /requirements.txt`

to run flash `arduino-input-handler.ino` to the arduino, set up the relay on pin 22, connected to the power supply and the fan, and run `python weather-checker.py`




[^1]:version 3.11 or above is fine, older versions may work but I haven't tested them





### Demo / screenshots:
![image](https://github.com/user-attachments/assets/14831461-5dd6-41dc-ac8c-5ffe76161be7)




##### The app was built for [Hack Club Arcade](https://hackclub.com/arcade/)
