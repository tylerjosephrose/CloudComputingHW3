# CloudComputingHW2
## Weather Database API
This API provides access to the maximum and minimum tempratures for every day that is stored in the database and returns in json.
The availbility is as follows  

Path | Data | Response | Types 
--- | --- | --- | ---
`<address>/api/historical/` | All dates available in the database | [{"DATE": 20130101},] | GET, POST
`<address>/api/historical/YYYYMMDD | The max and min temperatures for the date at the end of the request | {"DATE": 20130101, "TMAX": 34.0, "TMIN": 26.0} | GET, DELETE
`<address>/api/forecast/YYYYMMDD | The forecast for the next 7 days as predicted | [{"DATE": 20130101, "TMAX": 39.8, "TMIN": 22.2},{"DATE": 20130102, "TMAX": 42.7, "TMIN": 22.7},] | GET

Please note that the post request requires a post body of `{"DATE": <Date to set>, "TMAX": <temp to set>, "TMIN": <temp to set>}`
## Installation using virtualenv and existing database
---
**NOTE:** This installation is designed for a CentOS system or other system that uses systemctl to manage its services

---
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

## How To Use
Once you have it installed, you can hit your ip locally by going to your local ip and making any http requests as mentioned in the Weather Database API section. To see examples of python code that can hit the api's take a look at validate_hw2.py which can be used to verify that all of the provided apis work. The validate_hw2.py can by run with `python2 validate_hw2.py <address>/api`. If you are running validation from the same machine, the address can just be 127.0.0.1.
