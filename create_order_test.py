import requests
import configuration
import data


def get_order_track_number():

    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, headers=data.headers,
                             json=data.order_body)

    order_info = response.json()
    track_number = order_info.get("track_number")
    return track_number


def test_get_order_ifo_status_code_200():
    track_number = get_order_track_number()
    if isinstance(track_number, str):
        response = requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + track_number,
                                headers=data.headers)

        assert response.status_code == 200