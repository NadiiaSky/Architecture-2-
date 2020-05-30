from http.client import BAD_REQUEST

from flask import Blueprint, request, jsonify

from rest_api.controller import DateTimeController
from rest_api.utils import get_model_view

datetime_bp = Blueprint('date_time', __name__, url_prefix='')


def make_error_response(message, status='BAD_REQUEST', code=BAD_REQUEST):
    return jsonify({'status': status, 'description': message}), code


@datetime_bp.route('/create', methods=['POST'])
def create():
    data = request.json
    obj_type = data.pop('type')
    model, view = get_model_view(obj_type)
    if model is None or view is None:
        return make_error_response('incorrect object type')
    # dependency injection
    controller = DateTimeController(model, view)
    try:
        obj = controller.create_object(data)
    except (ValueError, TypeError) as e:
        return make_error_response(str(e))

    return jsonify({'status': 'OK', 'data': controller.make_response(obj)})
