from flask import Flask, jsonify, render_template
import requests
from numerize.numerize import numerize

app = Flask(__name__)

CHANNELS = {
  'cleverprogrammer': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
  'mrbeast': 'UCX6OQ3DkcsbYNE6H8uQQuVA',
  'mkbhd': 'UCBJycsmduvYEL83R_U4JriQ',
  'pm': 'UC3DkFux8Iv-aYnTRWzwaiBA',
}

ACTIVE_CHANNEL = CHANNELS['pm']




@app.route('/')
def index():
  url = "https://youtube138.p.rapidapi.com/channel/videos/"

  querystring = {"id":ACTIVE_CHANNEL,"hl":"en","gl":"US"}

  headers = {
    "X-RapidAPI-Key":      
    "46d41c07aamsh6052a8aa7ddcc90p1591d2jsn33358b5c8d59",
    "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)
  data = response.json()
  contents = data['contents']
  videos  = [video['video'] for video in contents if video['video']['publishedTimeText']]
  print(videos)
  video = videos[0]
  return render_template('index.html', videos=videos, video=video)

@app.template_filter()
def numberize(views):
  return numerize(views, 1)

@app.template_filter()
def highest_quality_image(thumbnails):
  return thumbnails[3]['url'] if len(thumbnails) >= 4 else thumbnails[0]['url']
  
app.run(host='0.0.0.0', port=81)