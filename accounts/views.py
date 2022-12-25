from django.contrib.auth import get_user_model
from accounts.forms import SignUpForm
from django.shortcuts import render


User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                User(email=email, password=raw_password)

                sucess = 'Você foi cadastrado com sucesso!'

                return render(request, 'core/message.html', {'message': sucess})
        except Exception as e:
            error = str(e)
            return render(request, 'core/message.html', {'message': error})

    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
