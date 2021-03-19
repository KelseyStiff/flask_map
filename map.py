import flask
from flask import request, url_for, render_template, redirect
import os
from state_centers import centers
from states_and_months import states, months
import national_parks_api
import sys


app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def my_maps():
  # parks = {"name": "yosemite", "coordinates": [37.8651,-119.538]}
  # key = os.environ.get('MAPBOX_KEY')
  key = 'pk.eyJ1Ijoia2l0dHlzdGlmZiIsImEiOiJjazZ2aDF3ZzcwMXNxM2hvMmJiZTlvaTI5In0.oEO-8s7LpbrCHJatQnXVKg'
  state_center = centers
  state = states
  month = months
  state_center = centers
  parks = []


  return render_template('index.html', key=key, state_center = state_center, month=month, state=state, parks=parks)

@app.route('/test',methods=['GET','POST'])
def test():
  if request.method == 'POST':
    state_input = request.form.get("states")
    month_input = request.form.get("months")

  if state_input and month_input:
    parks = national_parks_api.get_park_data(state_input,month_input)
    return render_template('test.html', parks=parks)











if __name__ == '__main__':
    app.run(debug=True)