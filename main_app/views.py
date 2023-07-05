from django.shortcuts import render

finches = [
    {'name': 'Jackson', 'type': 'American Goldfinch', 'description': 'pretty little guy', 'age': 2, 'alive': False},
    {'name': 'Beth', 'type': 'Black Rosy-Finch', 'description': 'silly goose! or should I say finch ;)', 'age': 3, 'alive': True},
    {'name': 'Matilda', 'type': 'Black-headed Grosbeak', 'description': 'Matilda isn''t actually real :(', 'age': 2, 'alive': False},
]
# Create your views here.

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def finch_index(request):
    return render(request, 'finches/index.html', {'finches': finches })