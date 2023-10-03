from celery import shared_task
from datetime import datetime
from myproject.mailing_app.models import Mailing


@shared_task
def send_mailing(mailing_id):
    try:
        # Получите рассылку по mailing_id
        mailing = Mailing.objects.get(pk=mailing_id)

        # Проверьте, должна ли рассылка быть отправлена в текущий момент
        current_time = datetime.now()
        if mailing.start_time <= current_time <= mailing.end_time:
            clients = mailing.clients.all()

            # Отправьте сообщение каждому клиенту
            for client in clients:
                pass


    except Mailing.DoesNotExist:
        pass