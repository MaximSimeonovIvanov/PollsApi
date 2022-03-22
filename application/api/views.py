from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PollSerializer
from .models import Poll


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Get all polls': '/poll/',
        'Create a poll': '/poll/',
        'Get a specific poll': '/poll/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def getAllOrCreate(request):
    if request.method == 'POST':
        serializer = PollSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'GET':

        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def getSpecificPollOrDelete(request, pk):

    if request.method == 'GET':
        if Poll.objects.filter(id=pk).exists():
            poll = Poll.objects.get(id=pk)
            serializer = PollSerializer(poll, many=False)
            return Response(serializer.data)
        else:
            return JsonResponse({'errorMessage': 'No such poll with specified id:' + pk + ' found', 'statusCode': 400})
    elif request.method == 'DELETE':
        if Poll.objects.filter(id=pk).exists():
            poll = Poll.objects.get(id=pk)
            poll.delete()
            return JsonResponse({'message': 'Successfully deleted poll'})
        else:
            return JsonResponse({'errorMessage': 'Cannot delete poll with specified id:' + pk, 'statusCode': 400})


