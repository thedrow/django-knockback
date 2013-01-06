from django.db.models import Model as DjangoModel

class Model(object):
    def __init__(self, model):
        if issubclass(type(model), DjangoModel):
            self.model = type(model)
            self.model_instance = model
        elif isinstance(model, type) and  issubclass(model, DjangoModel):
            self.model = model
            self.model_instance = None
        else:
            raise TypeError(
                'A django model type or instance was not provided. Found %s instance instead.' % model.__class__.__name__)

        fields = self.model._meta.fields

        self.idAttribute = self.model._meta.pk.name

        self.defaults = dict([(field.name, field.get_default()) for field
                              in fields if field.has_default()])

        if self.model_instance is not None:
            self.attributes = dict([(field.name, field.value_from_object(self.model_instance)) for field in fields])
        else:
            self.attributes = {}

__all__ = ['Model']