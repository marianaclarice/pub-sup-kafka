import os
import json
import logging
import smtplib
from email.message import EmailMessage
from confluent_kafka import Consumer, KafkaError

REMETENTE = os.environ['EMAIL_REMETENTE']
SENHA = os.environ['EMAIL_SENHA']
DESTINO = os.environ['EMAIL_DESTINO']

MENSAGENS = {
    'rotate': 'O arquivo {} foi rotacionado.',
    'grayscale': 'O arquivo {} foi convertido para preto e branco.',
}

def enviar_email(texto):
    msg = EmailMessage()
    msg['Subject'] = 'Notificação de processamento de imagem'
    msg['From'] = REMETENTE
    msg['To'] = DESTINO
    msg.set_content(texto)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(REMETENTE, SENHA)
        server.send_message(msg)
    logging.warning(f'E-mail enviado: {texto}')

c = Consumer({
    'bootstrap.servers': 'kafka1:19091,kafka2:19092,kafka3:19093',
    'group.id': 'notificador-group',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
})

c.subscribe(['notificacao'])

try:
    while True:
        msg = c.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            data = json.loads(msg.value())
            modelo = MENSAGENS.get(data['operation'])
            if modelo:
                try:
                    enviar_email(modelo.format(data['file']))
                except Exception as e:
                    logging.error(f'Falha ao enviar e-mail: {e}')
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            logging.warning('End of partition reached')
        else:
            logging.error('Error occured: {0}'.format(msg.error().str()))
except KeyboardInterrupt:
    pass
finally:
    c.close()