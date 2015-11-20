from django.db.models import Model, TextField


class AbstractRun(Model):
    class Meta:
        abstract = True

    endpoint = TextField()
    apikey = TextField()
    host = TextField()
    user = TextField()
    directory = TextField()
    command = TextField()


class BasicRun(AbstractRun):
    pass


class BitbucketRun(AbstractRun):
    repository = TextField()
    branch = TextField()

