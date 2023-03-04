from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
  'id': 1,
  'title': "Data analysis",
  'location': "CG"
}, 
  {
  'id': 2,
  'title': "Data reader",
  'location': "Raipur"
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


#return data in json formate
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
