from model.models import DateTime, Date
from rest_api.views import DateView, DateTimeView

OBJECTS_MAP = {
    'date': (Date, DateView),
    'datetime': (DateTime, DateTimeView),
}


def get_model_view(obj_type):
    return OBJECTS_MAP.get(obj_type, (None, None))
