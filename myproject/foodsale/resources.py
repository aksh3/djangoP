from import_export import resources
from .models import foodsale

class PersonResource(resources.ModelResource):
    class Meta:
        model = foodsale