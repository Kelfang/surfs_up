# Import dependencies.
import datetime as dt
import numpy as np
import pandas as pd

# Import additional dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask dependencies.
from flask import Flask, jsonify

# Create engine.
engine = create_engine("sqlite:///hawaii.sqlite")

# Define to reflect an existing database into a new model.
Base = automap_base()

# Reflect the database.
Base.prepare(engine, reflect=True)

# Save the references to each table.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database.
session = Session(engine)

# Define our Flask app.
app = Flask(__name__)

# Define the welcome route - 1st route. Add in the <p>, </p> for line breaks.
@app.route('/')
def welcome():
    return(
      '''
    Welcome to the Climate Analysis API!
    <p>Available Routes:</p>
    <p>/api/v1.0/precipitation/</p>
    <p>/api/v1.0/stations</p>
    <p>/api/v1.0/tobs</p>
    <p>/api/v1.0/temp/start/end</p>
    ''')

# Create the precipitation route and function - 2nd route. 
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# Create the stations route and function - 3rd route.
@app.route("/api/v1.0/stations")
def stations():
  results = session.query(Station.station).all()
  stations = list(np.ravel(results))
  return jsonify(stations=stations)

# Create the temperature route and function - 4th route.
@app.route("/api/v1.0/tobs")
def temp_monthly():
  prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
  results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all()
  temps = list(np.ravel(results))
  return jsonify(temps=temps)

# Create the minimum, average and max temperatures - 5th (last) route.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
  sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
  if not end:
    results = session.query(*sel).\
      filter(Measurement.date >= start).all().\
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

  results = session.query(*sel).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()
  temps = list(np.ravel(results))
  return jsonify(temps)