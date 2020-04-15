import logging
import requests

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/citySearch", methods=['POST'])
def Home():
    print(request.method)
    cName = request.form['cName']
    data = apiCalls(cName)
    print(cName)
    return render_template('result.html', data=data)


def apiCalls(cName):
    print('inside city search')
    print('inside apicalls', cName)
    print("type is", type(cName))
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country": "US"}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "7c844068f9msh8dbaa7c1f7887b5p1e7196jsn8a07f1641cc7"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    x = response.json()
    # check for response status code as 200 then put forward
    dataset = []
    for k in x['data']['covid19Stats']:
        if k['city'] == cName:
            data = [(k['city']), k['province'], print(k['country']), k['confirmed'], k['deaths'], k['recovered']]
            dataset.append(data)
            print(dataset)
    return dataset


@app.route("/countrySearch", methods=['POST'])
def Home1():
    print(request.method)
    coName = request.form['coName']
    data = apiCalls1(coName)
    print(coName)
    return render_template('result.html', data=data)


def apiCalls1(cName):
    print('inside apicalls', cName)
    print("type is", type(cName))
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country": cName}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "7c844068f9msh8dbaa7c1f7887b5p1e7196jsn8a07f1641cc7"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    x = response.json()
    print(x)
    # check for response status code as 200 then put forward
    dataset = []
    for k in x['data']['covid19Stats']:
        if k['city'] == '':
            data = [(k['city']), k['province'], (k['country']), k['confirmed'], k['deaths'], k['recovered']]
            dataset.append(data)
            print(dataset)
    return dataset


@app.route("/")
def Homepage():
    print(request.method)
    return app.send_static_file("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8002, debug=True)
