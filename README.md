# flask-prayer-times
small web app to get prayer times with offline calculation (no api used)
The app is published at http://vodaxe.pythonanywhere.com/
## Technologies Used
[Flask](https://pypi.org/project/Flask/)<br/>
[pyIslam](https://pypi.org/project/islam/)<br/>
[pytz](https://pypi.org/project/pytz/)<br/>
[TimezoneFinder](https://pypi.org/project/timezonefinder/)<br/>
[geopy](https://pypi.org/project/geopy/)(Note: The service used for this map is Nominatim wich belongs to open source openstreetmaps)<br/>

## How to use
Enter your city name<br/>
Choose asr fiqh according to your region (number 1 is nearly worldwide)<br/>
Choose asr fajr calc method according to region (it is important as angle determines fajr and asr time)<br/>
Then submit and you should have a table with prayer times and you can look another city if you like<br/>

You can also totally use it as an api and send POST requests to http://vodaxe.pythonanywhere.com/praytimes
args = {city, madhab ,calc_method}

## I totally accept new ideas and imrovements as well as bug reports<br/>I will try my best to keep this updated
## Note: I suck at ui/ux thats why i didnt style it. I will try do it in the future

# To-Do
[] add GET method  
[] make it into a full independant api (w json return)  
[] weekly/monthly/yearly prayers table  
[] Html/CSS design  
