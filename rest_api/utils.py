from rest_api.models import DateModel, DateTimeModel
from rest_api.views import DateView, DateTimeView

OBJECTS_MAP = {
    'date': (DateModel, DateView),
    'datetime': (DateTimeModel, DateTimeView),
}


def get_model_view(obj_type):
    return OBJECTS_MAP.get(obj_type, (None, None))
