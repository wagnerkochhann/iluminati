from nose.tools import assert_true
import requests
from datetime import datetime, timedelta

# baseUrl = "http://127.0.0.1"
baseUrl = "http://localhost:5000"
#baseUrl = "http://192.168.99.100:4200/api" #windows 10, docker toolbox assigned ip
# baseUrl = "https://python3-flask-uat.herokuapp.com/"
UUID = None


def test_get_all_cats():
    global baseUrl
    response = requests.get('%s/cats' % (baseUrl))
    assert_true(response.ok)


def test_get_individual_cat():
    global baseUrl
    response = requests.get(
        '%s/cats/1' % (baseUrl))
    assert_true(response.ok)


def test_get_individual_cat_404():
    global baseUrl
    response = requests.get('%s/cats/an_incorrect_id' % (baseUrl))
    assert_true(response.status_code == 404)


def test_add_new_cat():
    global baseUrl
    global UUID
    payload = {"cat": {
        'name': 'seanwasere',
        'genus': 'feline',
        'isHungry': True,
        'lastFedDate': datetime.now().timestamp()
    }}
    response = requests.post('%s/cats' % (baseUrl), json=payload)
    UUID = str(response.json()['cat']['id'])
    assert_true(response.status_code == 201)


def test_add_new_cat_unicode_cat_name():
    global baseUrl
    global UUID
    payload = {"cat": {
        'name': '▚Ⓜ⌇⇲',
        'genus': 'feline',
        'isHungry': True,
        'lastFedDate': None
    }}
    response = requests.post('%s/cats' % (baseUrl), json=payload)
    assert_true(response.ok)


def test_add_new_cat_no_cat_name():
    global baseUrl
    global UUID
    payload = {"cat": {
        'genus': 'feline',
        'isHungry': True,
        'lastFedDate': None
    }}
    response = requests.post('%s/cats' % (baseUrl), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_cat_no_cat_genus():
    global baseUrl
    global UUID
    payload = {"cat": {
        'name': '▚Ⓜ⌇⇲',
        'isHungry': True,
        'lastFedDate': None
    }}
    response = requests.post('%s/cats' % (baseUrl), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_cat_no_cat_ishungry():
    global baseUrl
    global UUID
    payload = {"cat": {
        'name': '▚Ⓜ⌇⇲',
        'genus': 'feline',
        'lastFedDate': None
    }}
    response = requests.post('%s/cats' % (baseUrl), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_cat_no_date():
    global baseUrl
    global UUID
    payload = {"cat": {
        'name': '▚Ⓜ⌇⇲',
        'genus': 'feline',
        'isHungry': True,
        'lastFedDate': None
    }}
    response = requests.post('%s/cats' % (baseUrl), json=payload)
    assert_true(response.status_code == 201)


def test_add_new_cat_no_payload():
    global baseUrl
    global UUID
    payload = None
    response = requests.post('%s/cats' % (baseUrl), json=payload)
    assert_true(response.status_code == 400)


def test_get_new_cat():
    global baseUrl
    global UUID
    url = '%s/cats/%s' % (baseUrl, UUID)
    response = requests.get(url)
    assert_true(response.ok)


def test_edit_cat_name():
    global baseUrl
    global UUID
    payload = {"cat": {
        'name': 'editedcatname',
        'genus': 'feline',
        'isHungry': True,
        'lastFedDate': None
    }}
    response = requests.put('%s/cats/%s' % (baseUrl, UUID), json=payload)
    name = str(response.json()['cat']['name'])
    assert_true(name == "editedcatname")


def test_edit_cat_genus():
    global baseUrl
    global UUID
    payload = {"cat": {
        'name': 'editedcatname',
        'genus': 'canine',
        'isHungry': True,
        'lastFedDate': None
    }}
    response = requests.put('%s/cats/%s' % (baseUrl, UUID), json=payload)
    genus = str(response.json()['cat']['genus'])
    assert_true(genus == "canine")


def test_edit_cat_isHungry():
    global baseUrl
    global UUID
    payload = {"cat": {
        'name': 'editedcatname',
        'genus': 'canine',
        'isHungry': False,
        'lastFedDate': None
    }}
    response = requests.put('%s/cats/%s' % (baseUrl, UUID), json=payload)
    isHungry = response.json()['cat']['isHungry']
    assert_true(isHungry == False)


def test_edit_cat_lastFedDate():
    global baseUrl
    global UUID
    payload = {"cat": {
        'name': 'editedcatname',
        'genus': 'canine',
        'isHungry': False,
        'lastFedDate': 101.1
    }}
    response = requests.put('%s/cats/%s' % (baseUrl, UUID), json=payload)
    lastFedDate = response.json()['cat']['lastFedDate']
    assert_true(lastFedDate == 101.1)

# def test_delete_new_record():
#     global baseUrl
#     global UUID
#     response = requests.delete('%s/cats/%s' % (baseUrl, UUID))
#     assert_true(response.status_code == 204)


# def test_delete_new_record_404():
#     global baseUrl
#     global UUID
#     response = requests.delete('%s/cats/%s' % (baseUrl, UUID))
#     assert_true(response.status_code == 404)
