import requests
from plyer import notification


API_KEY = "02b5554c7aecf8b4d4e8b391a56cc6db2e648197730b4a097107c51454aa"


def getData():
    r = requests.get('https://ethgasstation.info/api/ethgasAPI.json?api-key=' + API_KEY)

    json = r.json()

    safeLow = str(json['safeLow'])
    fastest = str(json['fastest'])

    return([safeLow, fastest])

data = getData()
notification.notify(
    title='Current prices for gas',
    message='Low: ' + data[0] + ' Fastest: ' + data[1],
)
