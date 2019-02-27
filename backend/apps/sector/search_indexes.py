from haystack import indexes
from apps.sector.models import Sector


class SectorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    name_auto = indexes.EdgeNgramField(model_attr='name')
    standardized = indexes.BooleanField(model_attr='standardized')

    def get_model(self):
        return Sector

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
