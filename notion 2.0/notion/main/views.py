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
    if request.method == "POST":
        form = NotionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NotionForm()
    return render(request, 'main/add_note.html', {'form': form})
