from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Music
from .serializers import MusicSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def music_list(request):
    if request.method == 'GET':
        songs = Music.objects.all()
        serializer = MusicSerializer(songs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def product_detail(request, pk):
    song = get_object_or_404(Music,pk=pk)
    if request.method == 'GET':
        serializer = MusicSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(song,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response('the song is deleted', status=status.HTTP_204_NO_CONTENT)
    
