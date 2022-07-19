from pyexpat import model
from import_export import resources
from accounts.models import Book, Students

class StudentResources(resources.ModelResource):
    class Meta:
        model = Students


class BookResources(resources.ModelResource):
    class Meta:
        model = Book