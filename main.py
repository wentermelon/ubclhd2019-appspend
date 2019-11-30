# Our Backend for the App!
# Built with Flask

# Import Flask
import flask
import requests

# Create the application
app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

# path parameters
@app.route('/<name>')
def personal_hello(name):
    return "Hello " + name + "."

# serving hello.html
@app.route('/fancy/<name>')
def some_page(name):
    return flask.render_template('hello.html', name=name)

# serving find.html
@app.route('/find', methods=['GET'])
def find():
    return flask.render_template('find.html')

# process query
@app.route('/process_query', methods=['post'])
def process_query():
    data = flask.request.form
    location = data['some_location']

    requestString = formRequest(location)
    responses = makeGET(requestString)['candidates']
    return flask.render_template('find.html', responses=responses)

def formRequest(input):

    API_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?inputtype=textquery&locationbias=ipbias&fields=formatted_address,name,rating&"

    return API_URL + "key={k}&input={i}".format(k=readKey(), i=input)

def makeGET(input):
    response = requests.get(input)

    if response:
        return response.json()
    else:
        return "Error GETting that URL. Check to see if it is well-formed?"

def readKey():
    f = open("secrets.txt", "r")
    contents = f.read()
    return contents.strip()

if __name__ == '__main__':
    app.run(debug=True)
