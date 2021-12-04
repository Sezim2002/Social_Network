from social_network.celery import app

@app.task
def send_activation_mail(email, activation_code):
    from django.core.mail import send_mail
    message = f'Ваш код активации: {activation_code}'
    send_mail('Активация аккаунта', message, 'maitukinovva02@gmail.com', [email])