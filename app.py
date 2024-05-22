from bottle import Bottle, run, template, static_file

# Create a Bottle app instance
app = Bottle()

# Route for serving static files
@app.route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='./static')

# Define a route for the home page
@app.route('/')
def home():
    return template('home', name='World')

# Define a route for a dynamic greeting
@app.route('/hello/<name>')
def greet(name):
    return template('greet', name=name)

# Run the app on localhost, port 8080
if __name__ == '__main__':
    run(app, host='localhost', port=8080)