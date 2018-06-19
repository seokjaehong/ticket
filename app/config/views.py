import mimetypes
import os

from django.contrib.auth import get_user_model
from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from config import settings
from ticket.models.ticketdata import TicketData


def index(request):
    tickets = TicketData.objects.all()
    context = {
        'tickets': tickets
    }
    return render(request, 'base.html', context)


def serve_media(request, path):
    media_path = os.path.join(settings.MEDIA_ROOT, path)
    content_type = mimetypes.guess_type(path)
    # return HttpResponse(media_path)
    return FileResponse(
        open(media_path, 'rb')
        , content_type=content_type,
    )
