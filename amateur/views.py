from django.shortcuts import render
from django.template import loader

from .models import ChatMessage

from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    room = request.GET.get('room', 'Todos')
    messages = ChatMessage.objects.filter(room=room).order_by('time')
    template = loader.get_template('amateur/index0.html')
    context = {
        'messages': messages,
    }
    return HttpResponse(template.render(context, request))

def phone(request):
    template = loader.get_template('amateur/index.html')
    return HttpResponse(template.render({}, request))

@csrf_exempt
def guardamsg(request):
    cuarto = request.POST.get('room', None)
    usuario = request.POST.get('user', None)
    mensaje = request.POST.get('msg', None)
    ChatMessage.objects.create(
    	room=cuarto,
    	message=mensaje,
    	user=usuario
    )
    data = {
    'is_saved': ChatMessage.objects.filter(room__iexact=cuarto).filter(message__iexact=mensaje).filter(user__iexact=usuario).exists()
    }
    return JsonResponse(data)
