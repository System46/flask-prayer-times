"""Python Flask Web App to get prayer times"""
########################[Imports]######################
from flask import Flask, render_template, url_for , request
from datetime import date
import datetime
from geopy.geocoders import Nominatim
from pyIslam.praytimes import (
    PrayerConf,
    Prayer,
    LIST_FAJR_ISHA_METHODS,
)
from pyIslam.hijri import HijriDate
from pyIslam.qiblah import Qiblah
from timezonefinder import TimezoneFinder
import pytz
########################[Main Variables]###############
app = Flask(__name__)
geolocator = Nominatim(user_agent='prayer-times')
tf = TimezoneFinder()
#----------[salaah calculation]-----------------------#
madhabs = ("1- Shafii, Maliki, Hambali", "2- Hanafi")

####################[Routes]###########################

@app.route("/") #=> index page where user can choose his city
def index():
    fajr_isha_calc=[]
    for method in LIST_FAJR_ISHA_METHODS:
        fajr_isha_calc.append("{} = {}".format(method.id, " | ".join(method.organizations)))
    return render_template('select.html', madhabs=madhabs, calc_methods=fajr_isha_calc)

@app.route('/praytimes',methods = ['POST', 'GET']) #=> api to handle prayer times requests
def result():
   if request.method == 'POST':
       location = geolocator.geocode(request.form['city'])
       ct = datetime.datetime.now() 
       timezone = float(pytz.timezone(tf.timezone_at(lng=location.longitude, lat=location.latitude)).utcoffset(datetime.datetime(ct.year, ct.month, ct.day, ct.hour, ct.minute, ct.second)).total_seconds()/3600)
       pt = Prayer(PrayerConf(location.longitude, location.latitude, timezone, int(request.form['calc_method'][:1]), int(request.form['madhab'][:1])), date.today())
       prayer_times = {
           "Fajr": pt.fajr_time(),
           "Sherook": pt.sherook_time(),
           "Dohr" : pt.dohr_time(),
           "Asr" : pt.asr_time(),
           "Maghreb":pt.maghreb_time(),
           "Ishaa":pt.ishaa_time(),
           "Qiyam":pt.last_third_of_night()}
       return render_template("prayers.html", city=request.form['city'], prayers=prayer_times)

####################[Running]###########################
if __name__ == '__main__':
    app.run(debug=True)