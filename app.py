from flask import Flask , render_template , jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'data analyst',
    'location':'bengaluru,india',
    'salary':'Rs.10,00,000'
  },
  {
    'id':2,
    'title':'frontend developer',
    'location':'pune,india',
    'salary':'Rs.8,00,000'
  },
  {
    'id':3,
    'title':'backend developer',
    'location':'delhi,india',
    'salary':'Rs.8,50,000'
  },
  {
    'id':4,
    'title':'ui/ux designer',
    'location':'remote',
    'salary':'Rs.5,00,000'
  },
]

@app.route('/')

def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0' , debug=True)