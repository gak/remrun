from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from web import tasks
from web.bitbucket import should_run_bitbucket
from web.models import AbstractRun, BasicRun, BitbucketRun


@api_view(['POST'])
def run_view(request, endpoint):
    try:
        run = AbstractRun.objects.get_subclass(endpoint=endpoint)
    except ObjectDoesNotExist as e:
        raise Http404(e)

    if request.GET.get('apikey') != run.apikey:
        raise AuthenticationFailed('API key mismatch')

    do_it, reason = should_run(request, run)
    if do_it:
        # Synchronous for now...
        kwargs = {
            'kwargs': {
                'user': run.user,
                'directory': run.directory,
                'command': run.command,
            },
            'queue': 'runrem-{}'.format(run.host),
        }
        print('Running: {}'.format(kwargs))
        tasks.run.apply_async(**kwargs)

        return Response({
            'did_execute': True,
        })

    else:
        return Response({
            'did_execute': False,
            'reason': reason,
        })


def should_run(request, run):
    if isinstance(run, BasicRun):
        return True, None

    if isinstance(run, BitbucketRun):
        return should_run_bitbucket(request, run)

    raise Exception('Unknown run type: {}'.format(run.__class__))
