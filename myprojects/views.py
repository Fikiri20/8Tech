from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from academic.models import PastPapers, Notes
import os


def download_past_paper(request, file_id):

    past_paper = get_object_or_404(PastPapers, id=file_id)
    full_file_path = past_paper.past_paper_file.path

    if os.path.exists(full_file_path):

        return FileResponse(open(full_file_path, 'rb'), as_attachment=True, filename=os.path.basename(full_file_path)) 
    else:
        return Http404("File doesn't exist ")
    

def download_note(request, file_id):

    note = get_object_or_404(Notes, id=file_id)
    full_file_path = note.notes_file.path

    if os.path.exists(full_file_path):

        return FileResponse(open(full_file_path, 'rb'), as_attachment=True, filename=os.path.basename(full_file_path)) 
    else:
        return Http404("File doesn't exist ")
    
    