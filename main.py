from flask import Flask, render_template, url_for, request, redirect, send_from_directory

from data import data
import datetime


app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html",data=data)

@app.route('/reportscam/', methods =["GET", "POST"])
def report(data=data):
  if request.method == "POST":
    name = request.form.get("name")
    how = request.form.get("how")
    country = request.form.get("country")
    lat = request.form.get("lat")
    long = request.form.get("lon")
    avoid = request.form.get("avoid")
    title = request.form.get("title")
    date =datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M")
    
    string = f"<b>{title} in {country}</b><br>{how}<br><br>{avoid}<br>     by {name}  {date} UTC"
    data.append([string,lat,long])
  

    with open('data.py', 'w') as f:
      f.write("data = "+str(data))

    
    return redirect(url_for("index"))
  
  return render_template("reportscam.html",data=data)



app.run(host='0.0.0.0', port=81)