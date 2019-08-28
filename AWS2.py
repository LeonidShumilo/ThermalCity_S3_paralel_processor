import pika
import psycopg2
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import os
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channe2 = connection.channel()
api = SentinelAPI('MRDEVISH', 'Research1')
channel.queue_declare(queue='AWS2')
connection1 = psycopg2.connect(user="postgres",
                                  password="Research1",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="db_products")


def callback(ch, method, properties, body):
    #ch.basic_ack()
    cursor1 = connection1.cursor()
    query0 = """select "Product Name" from "Products" where "Processed"=0; """
    cursor1.execute(query0)
    records = cursor1.fetchone()
    for i in range(body,len(records),2):
        api.download(records[i])
        cursor1 = connection1.cursor()
        os.system('gpd processing.xml -Input1 = {} -Input2 = {}'.format(records[i],record[i]))
        query0 = """UPDATE "Products" SET "Processed"=1 WHERE "Product Name"={};""".format(record[i])
    #channel.stop_consuming()
    
    #ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()