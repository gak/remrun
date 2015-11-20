from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from web.models import AbstractRun


@api_view(['POST'])
def run_view(request, endpoint):
    try:
        run = AbstractRun.objects.get(endpoint=endpoint)
    except ObjectDoesNotExist as e:
        raise Http404(e)
    return Response({'a': run.command})
