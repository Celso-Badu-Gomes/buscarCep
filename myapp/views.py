from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Endereco
from .forms import EnderecoForm
from django.shortcuts import redirect
import pycep_correios

# Create your views here.

def endereco_list(request):
    enderecos = Endereco.objects.all()
    return render(request, 'myapp/endereco_list.html', {'enderecos': enderecos})

def endereco_detail(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)
    return render(request, 'myapp/endereco_detail.html', {'endereco': endereco})
    
def endereco_new(request):
    if request.method == "POST":
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.save()
            return redirect('endereco_detail', pk=endereco.pk)
    else:
        form = EnderecoForm()
    return render(request, 'myapp/endereco_edit.html', {'form': form})
    
def endereco_edit(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)
    if request.method == "POST":
        form = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.save()
            return redirect('endereco_detail', pk=endereco.pk)
    else:
        form = EnderecoForm(instance=endereco)
    return render(request, 'myapp/endereco_edit.html', {'form': form})
    
def endereco_remove(request, pk):
    endereco = get_object_or_404(Endereco, pk=pk)
    endereco.delete()
    return redirect('endereco_list')    
    
def busca_cep(request):
    if request.method == "POST":
        print('passei aqui')
        cep = request.POST['cep']
        ender = pycep_correios.consultar_cep(cep)

        data = {
            'estado': ender['uf'],
            'cidade': ender['cidade'],
            'logradouro': ender['end'],
            'bairro': ender['bairro'],
            'cep': ender['cep'],
        }
        form = EnderecoForm(data)
        return render(request, 'myapp/endereco_edit.html',{'form': form})
    else:
        return render(request, 'myapp/busca_cep.html', {})