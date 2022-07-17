import pika
#메시지를 전달하는 producer 받는사람 consumer

params=pika.URLParameters('amqps://fjvkdaue:jh8R7Ttv1uLeUyrvDaMFCBdMOK9axtMW@chimpanzee.rmq.cloudamqp.com/fjvkdaue')

connection=pika.BlockingConnection(params) # 레빗엠큐에 커넥션

channel= connection.channel()#채널 생성

def publish():#메시지를 어디로 전달할지에 대한 함수
    channel.basic_publish(exchange='',routing_key='order',body='hello')
    #가장 기초적인 메시지만 전달 order에 hello라는 텍스트를 전달 하고 싶다 