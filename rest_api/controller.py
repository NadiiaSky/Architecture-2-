class DateTimeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_object(self, data):
        return self.model(**data)

    def make_response(self, obj):
        return self.view.generate_response(obj)
