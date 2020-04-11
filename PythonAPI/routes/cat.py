from flask import jsonify, abort, request, Blueprint
from datetime import datetime, timedelta

cat = Blueprint('cat', __name__)


def get_blueprint():
    return cat


cats = [
    {
        'id': 1,
        'name': u'Cosmo',
        'genus': u'felis',
        'isHungry': True,
        # yesterday
        'lastFedDate': (datetime.today() - timedelta(1)).timestamp()
    },
    {
        'id': 2,
        'name': u'Emmy',
        'genus': u'felis',
        'isHungry': True,
        # yesterday
        'lastFedDate': (datetime.today() - timedelta(1)).timestamp()
    }
]


@cat.route('/cats', methods=['GET'])
def get_cats():
    return jsonify({'cats': cats})


@cat.route('/cats/<int:id>', methods=['GET'])
def get_cat(id):
    cat = [cat for cat in cats if cat['id'] == id]
    if len(cat) == 0:
        abort(404)
    return jsonify({'cat': cat[0]})


@cat.route('/cats', methods=['POST'])
def create_cat():
    if not request.get_json():
        abort(400)

    data = request.get_json(force=True)
    if not data['cat']:
        abort(400)
    elif not('name' in data['cat'] and type(data['cat']['name']) == str):
        abort(400)
    elif not('genus' in data['cat'] and type(data['cat']['genus']) == str):
        abort(400)
    elif not('isHungry' in data['cat'] and type(data['cat']['isHungry']) == bool):
        abort(400)
    elif not(len(data['cat']['name']) >= 3 and len(data['cat']['name']) <= 20):
        abort(400)

    cat = {
        'id': cats[-1]['id'] + 1,
        'name': data['cat']['name'],
        'genus': data['cat']['genus'],
        'isHungry': bool(data['cat']['isHungry']),
        'lastFedDate': data['cat']['lastFedDate']
        or datetime.now().timestamp()
    }
    # print(cat)
    cats.append(cat)
    return jsonify({'cat': cat}), 201


@cat.route('/cats/<int:id>', methods=['PUT'])
def update_cat(id):
    cat = [cat for cat in cats if cat['id'] == id]
    if len(cat) == 0:
        abort(404)

    if not request.get_json():
        abort(400)

    data = request.get_json(force=True)
    if not(data['cat']):
        abort(400)
    elif not('name' in data['cat'] and type(data['cat']['name']) == str):
        abort(400)
    elif not('genus' in data['cat'] and type(data['cat']['genus']) == str):
        abort(400)
    elif not('isHungry' in data['cat'] and type(data['cat']['isHungry']) == bool):
        abort(400)
    elif not(len(data['cat']['name']) >= 3 and len(data['cat']['name']) <= 20):
        abort(400)

    cat[0]['name'] = data['cat']['name']
    cat[0]['genus'] = data['cat']['genus']
    cat[0]['isHungry'] = data['cat']['isHungry']
    cat[0]['lastFedDate'] = data['cat']['lastFedDate'] or datetime.now().timestamp()
    #print(cats)
    return jsonify({'cat': cat[0]})


@cat.route('/cats/<int:id>', methods=['DELETE'])
def delete_cat(id):
    cat = [cat for cat in cats if cat['id'] == id]
    if len(cat) == 0:
        abort(404)
    cats.remove(cat[0])
    return ('', 204)
