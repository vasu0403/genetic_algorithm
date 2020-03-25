import json
import requests
import numpy as np

######### DO NOT CHANGE ANYTHING IN THIS FILE ##################
API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11

# functions that you can call


def get_errors(id, vector):
    """
    returns python array of length 2 
    (train error and validation error)
    """
    for i in vector:
        assert -10 <= abs(i) <= 10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))


def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector:
        assert -10 <= abs(i) <= 10
    assert len(vector) == MAX_DEG
    return send_request(id, vector, 'submit')

# utility functions


def urljoin(root, port, path=''):
    root = root + ':' + str(port)
    if path:
        root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root


def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, PORT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id': id, 'vector': vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response


if __name__ == "__main__":
    """
    Replace "test" with your secret ID and just run this file 
    to verify that the server is working for your ID.
    """

    err = get_errors('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', [-2.9571421994993077e-13, 8.512477622723832, -1.7463153512019917e-14, 0.04543092441535113, -1.3166021101108983e-13, 9.268383614250803e-14, -7.439202914623583e-14, 1.0418559140503912e-12, -2.1444592822341143e-13, 5.36764406322044e-13, -3.0727748074660687e-15])
    assert len(err) == 2
    print(err)

    # submit_status = submit('se1Poy6HllKuLEK3WlsQnfi6qAN6zt5JqbUgbchBylLc0FmRf2', [1.2138511353859433e-14, 8.512477622723907, -2.0318474043264225e-13, 0.049339031446866126, -1.0395200957365075e-13, -1.908593649732321e-13, -1.8816820059208847e-13, 1.1202370514512557e-12, -3.0938616696246473e-13, 1.721751443988186e-13, -7.0073964373864045e-15])
    # print(submit_status)
