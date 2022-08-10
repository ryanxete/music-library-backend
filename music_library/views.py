from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import MusicSerializer
from rest_framework import status


@api_view(['GET'])
def music_list(request):

    return Response('yea')