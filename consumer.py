#메시지를 받는 사함
import pika
#메시지를 전달하는 producer 받는사람 consumer

params=pika.URLParameters('amqps://fjvkdaue:jh8R7Ttv1uLeUyrvDaMFCBdMOK9axtMW@chimpanzee.rmq.cloudamqp.com/fjvkdaue')

connection=pika.BlockingConnection(params) # 레빗엠큐에 커넥션

channel= connection.channel()#채널 생성

channel.queue_declare(queue='order') # 브로커가 가지고 있는 메서드의 집함체 order에 있는 메시지만 받음

def callback(ch,method, properties,body):
    print('receive in order')#order가 받음
    print(body)

channel.basic_consume(queue='order',on_message_callback=callback) # 어떻게 consuming할지 선언
print('started consuming')

channel.start_consuming()
channel.close()