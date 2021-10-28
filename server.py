# /////////////////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python > Flask > Fundamentals: Playground
# By: Virgilio D. Cabading Jr.  Created: October 27, 2021
# /////////////////////////////////////////////////////////////////////

from flask import Flask, render_template                # Import Flask to allow us to create our app
app = Flask(__name__)                                   # Create a new instance of the Flask class called "app"

# **** Default App Route **********************************************
@app.route('/')                                         # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')

# **** Create a route that responds with the given word repeated as many times as specified in the URL ****
# @app.route('/repeat/<int:iterations>/<string:message>')
# def repeat_message (iterations, message):
#     return render_template('repeat.html', message=message, iterations=iterations)

# **** Play App Route *************************************************
@app.route('/play')
def play():
    return render_template('play.html')

# **** Play Iterations App Route *************************************************
@app.route('/play/<int:iterations>')
def play_iterations(iterations):
    return render_template('play_iterations.html', iterations=iterations)

# **** Play Iterations Color App Route *************************************************
@app.route('/play/<int:iterations>/<string:color>')
def play_iterations_color(iterations,color):
    return render_template('play_iterations_color.html', iterations=iterations, color=color)

# **** Handle invalid routes ******************************************
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



