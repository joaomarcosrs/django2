from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto, Upload

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = (f'Nome: {nome}\n'
                    f'E-mail: {email}\n'
                    f'Assunto: {assunto}\n'
                    f'Mensagem: {mensagem}')
        mail = EmailMessage(
            subject='E-mail enviado pelo django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br', ],
            headers={'Reply-To': email}
        )
        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque']

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['imagem']