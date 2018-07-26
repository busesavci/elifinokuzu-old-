from django.shortcuts import render, redirect
from dictionary.models import Node,Edge
from django.urls import reverse
from .forms import SubmissionForm


def home(request):
    nodes = Node.objects.all()

    # home.html dosyasına değişken yolluyoruz.
    return render(request, 'home.html', {
        'title': 'Öküzün Elifi',
        'nodes': nodes,
    })

def node_detail(request, id):
    node = Node.objects.get(id=id)
    incoming = node.incoming.all()
    outgoing = node.outgoing.all()

    # node_detail.html dosyasına değişken yolluyoruz.
    return render(request, 'node_detail.html', {
        'node': node,
        'incoming': incoming,
        'outgoing': outgoing,
        'title': 'Öküzün Elifi: %s' % node.name,
    })

def about(request):
    return render(request, 'about.html')

def support(request):
    return render(request, 'support.html')

def submit(request):
    form = SubmissionForm()

    if request.method == "POST":
        form=SubmissionForm(request.POST)

        if form.is_valid():
            source_node = Node.objects.create(
                name=form.cleaned_data['source_node'],
                language=form.cleaned_data['source_language'],
            )
            target_node = Node.objects.create(
                name=form.cleaned_data['target_node'],
                language=form.cleaned_data['target_language'],
            )
            edge = Edge.objects.create(
                source=source_node,
                destination=target_node,
                is_directed=False,
                type_of_edge=form.cleaned_data['type_of_edge'],
                resource=form.cleaned_data['resource'],
            )
            return redirect(reverse("node_detail", args=[source_node.id]))

    return render(request, 'submit.html',{"form":form})