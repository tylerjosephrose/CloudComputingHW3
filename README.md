# CloudComputingHW3
## Weather Forecast Website
This site has a form to select the date the user wants to display the forcast for. When the form is submitted, a table appears through ajax that displays the predicted maximum and minimum temperature for the next seven days started at the date input by the user. The website can be found at `<address>/forecast`
## Installation using virtualenv and existing database
1. Clone this repository to a directory of your choosing
2. cd into the directory with the code (you know you're in the right directory if you see manage.py in the directory)
3. Run the following commands to activate the virtual environment  
`virtualenv venv --distribute`  
`source venv/bin/activate`
4. Start the app `sudo python3 manage.py runserver 0.0.0.0:80`

##Installation without virtualenv and reloading database
1. Clone this repository to a directory of your choosing
2. cd into the directory with the code (you know you're in the right directory if you see manage.py in the directory)
3. Install all requirements with `python3 -m pip install -r requirements.txt`
4. Load the fixture which has all the original weather information in it `python3 manage.py loaddata Forecast/fixtures.json`
5. Start the app `sudo python3 manage.py runserver 0.0.0.0:80`

---
**NOTE:** If you plan to use a port other than port 80, make sure you go into the WeatherDatabase/settings.py and change the URL setting to the port you are using

---

## How To Use
Once you have it installed, you can view the website by navigating to the `<address>/forecast` where address is the address of the machine you installed it on. If you are on the same machine, you can just go to 127.0.0.1/forecast. From here you select your date using the dropdowns and hit submit. The table will then appear underneath the form.
