from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
# print(__name__)


@app.route('/')
def myhome():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt", mode="a") as db:
        # extract information from 'data' argument and write to the file
        email = data["email"]  # in dict format, extract value by key
        subject = data["subject"]
        message = data["message"]

        db.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as csv_file:
        # extract information from 'data' argument and write to the file
        email = data["email"]  # in dict format, extract value by key
        subject = data["subject"]
        message = data["message"]
        csvwriter = csv.writer(csv_file, delimiter=',',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        # return 'Form submitted Horray!!!'
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!'
