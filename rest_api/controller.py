class DateTimeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_object(self, data):
        self.model.validate(data)
        obj = self.model(**data)
        obj.save()
        return obj

    def make_response(self, obj):
        return self.view.generate_response(obj)
