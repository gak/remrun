from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from web import tasks
from web.models import AbstractRun, BasicRun, BitbucketRun


class ParseBitbucketRequestException(RuntimeError):
    pass


@api_view(['POST'])
def run_view(request, endpoint):
    try:
        run = AbstractRun.objects.get_subclass(endpoint=endpoint)
    except ObjectDoesNotExist as e:
        raise Http404(e)

    do_it, reason = should_run(request, run)
    if do_it:
        # Synchronous for now...
        tasks.run(run.user, run.directory, run.command)

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


def should_run_bitbucket(request, run):
    data = request.data

    try:
        repository = data['repository']['name']
    except KeyError as e:
        return False, 'Request did not have a repository/name: {}'.format(data)

    try:
        ref_changes = data['refChanges']
    except KeyError as e:
        return False, 'Request did not have a refChanges: {}'.format(data)

    if run.repository != repository:
        return False, 'Repository did not match "{}" != "{}"'.format(
            run.repository, repository,
        )

    good = False
    saw = []
    for ref_change in ref_changes:
        branch = ref_change['ref_id'].split('/')[-1]
        saw.append(branch)
        if branch == run.branch:
            good = True

    if not good:
        return False, \
            'No matching branches in refChanges. Wanted: {} Saw: {}'.format(
                run.branch, ','.join(saw)
            )

    if run.branch != branch:
        return False, 'Branch did not match "{}" != ""'.format(
            run.branch, branch,
        )

    return True, None
