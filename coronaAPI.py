import logging
import requests
import os
from flask import Flask, request, render_template

app = Flask("COVID-19 Tracker")


def rapidAPI(coName="US"):
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    querystring = {"country": coName}
    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "7c844068f9msh8dbaa7c1f7887b5p1e7196jsn8a07f1641cc7"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    x = response.json()
    return x


def unique(list1):
    # intilize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


# search by city

@app.route("/citySearch", methods=['POST'])
def Home():
    print(request.method)
    cName = request.form['cName']
    data = apiCalls_city(cName)
    print(cName)
    return render_template('result.html', data=data)


def apiCalls_city(cName):
    x = rapidAPI()
    dataset = []
    for k in x['data']['covid19Stats']:
        if k['city'] == cName:
            data = [(k['city']), k['province'], (k['country']), k['confirmed'], k['deaths'], k['recovered']]
            dataset.append(data)
            print(dataset)
    return dataset


# search by province

@app.route("/provinceSearch", methods=['POST'])
def Home_province():
    print(request.method)
    pName = request.form['pName']
    data = apiCalls_province(pName)
    print(pName)
    return render_template('result.html', data=data)


def apiCalls_province(pName):
    x = rapidAPI()
    dataset = []
    for k in x['data']['covid19Stats']:
        if k['province'] == pName:
            data = [(k['city']), k['province'], (k['country']), k['confirmed'], k['deaths'], k['recovered']]
            dataset.append(data)
            print(dataset)
    return dataset


# search by country
@app.route("/countrySearch", methods=['POST'])
def Home1():
    print(request.method)
    coName = request.form['coName']
    data = apiCalls_country(coName)
    print(data)
    return render_template('result.html', data=data)


def apiCalls_country(cName):
    x = rapidAPI(cName)
    # check for response status code as 200 then put forward
    dataset = []
    for k in x['data']['covid19Stats']:
        data = [(k['city']), k['province'], (k['country']), k['confirmed'], k['deaths'], k['recovered']]
        dataset.append(data)
        print(dataset)
        print("this is indside api calls")
    return dataset

# index page
@app.route("/")
def Homepage():
    data1 = unique_city()
    data2 = unique_country()
    data3 = unique_province()
    return render_template("index.html", data1=data1, data2=data2, data3=data3)


def unique_city():
    x = rapidAPI()
    # check for response status code as 200 then put forward
    dataset = []
    for k in x['data']['covid19Stats']:
        data = k['city']
        dataset.append(data)
    # print("this is index dataset", dataset)
    x = unique(dataset)
    print("city", x)
    return x


def unique_country():
    x = rapidAPI('')
    # check for response status code as 200 then put forward
    dataset = []
    for k in x['data']['covid19Stats']:
        data = k['country']
        dataset.append(data)
    x = unique(dataset)
    return x


def unique_province():
    x = rapidAPI()
    # check for response status code as 200 then put forward
    dataset = []
    for k in x['data']['covid19Stats']:
        data = k['province']
        dataset.append(data)
    x = unique(dataset)
    return x


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8082, debug=True)
