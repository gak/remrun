import shortuuid
from django.db.models import Model, CharField


def new_shortuuid():
    return shortuuid.uuid()


class AbstractRun(Model):
    class Meta:
        abstract = True

    endpoint = CharField(max_length=100, unique=True)
    apikey = CharField(max_length=100, default=new_shortuuid)
    host = CharField(max_length=100)
    user = CharField(max_length=100)
    directory = CharField(max_length=1000)
    command = CharField(max_length=1000)


class BasicRun(AbstractRun):
    pass


class BitbucketRun(AbstractRun):
    repository = CharField(max_length=100)
    branch = CharField(max_length=100)
