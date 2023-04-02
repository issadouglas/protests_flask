"""basic Flask app - demo of using a variable in a route"""
from flask import Flask, render_template
app = Flask(__name__)

import csv

def convert_to_dict(filename):
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # create DictReader object
    my_reader = csv.DictReader(datafile)

    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)

    # close original csv file
    datafile.close()

    # return the list
    return list_of_dicts

protest_list = convert_to_dict('protests.csv')

pairs_list =[]
for protest in protest_list:
    pairs_list.append((protest['ID'],protest['protest_name']))



@app.route('/')
def index():

    return render_template('index.html', pairs=pairs_list)

@app.route('/protest_name/<num>')
def protest_name(num):
    protest = protest_list[int(num) - 1]
    return render_template('protest.html', protest = protest )

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=4999, debug=True)
