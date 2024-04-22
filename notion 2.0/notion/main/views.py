from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')


def note_list(request):
    notes = Notion.objects.all()
    return render(request, 'main/layout.html', {'notes': notes})

def add_note(request):
    notes = Notion.objects.all()
    if request.method == "POST":
        form = NotionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NotionForm()
    return render(request, 'main/add_note.html', {'form': form, 'notes': notes})


def note_detail(request, note_id):
    note = get_object_or_404(Notion, pk=note_id)
    notes = Notion.objects.all()  # Получаем все заметки
    return render(request, 'main/note_detail.html', {'note': note, 'notes': notes})
