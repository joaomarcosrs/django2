from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .forms import ContatoForm, ProdutoModelForm, UploadModelForm
from .models import Produto, Upload

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'E-mail enviado com suceso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar E-mail!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso!')
                form = ProdutoModelForm()
            else:
                messages.success(request, 'Erro ao salvar produto!')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }

        return render(request, 'produto.html', context)
    else:
        return redirect('index')

def image_upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        if settings.USE_S3:
            upload = Upload(imagem=image_file)
            upload.save()
            image_url = upload.imagem.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        context = {
            'form': image_url
        }
        return render(request, 'upload.html', context)
    return render(request, 'upload.html')