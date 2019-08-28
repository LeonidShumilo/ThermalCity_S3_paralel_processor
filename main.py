import datetime
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import psycopg2

api = SentinelAPI('MRDEVISH', 'Research1')
today_date = datetime.date.today()
footprint = geojson_to_wkt(read_geojson('search_polygon_10.geojson'))
platformname = 'Sentinel-3'
producttype='SL_2_LST___'
products = api.query(footprint,platformname=platformname,producttype=producttype, date = (today_date-1,today_date))
products_pandas = api.to_geodataframe(products)
Names = products_pandas['Product Name']
connection1 = psycopg2.connect(user="postgres",
                                  password="Research1",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="db_products")
cursor1 = connection1.cursor()
query0 = """select "Product Name" from "Products"; """
cursor1.execute(query0)
records = cursor1.fetchone()
num=1
undownloaded = []
for i in Names:
    if i not in records:
        cursor1 = connection1.cursor()
        id_ = len(records)+num
        query = """INSERT INTO "Products" Values({},{},{},0);""".format(id_,i,today_date)
        cursor1.execute(query0)
        num=num+1
import pika
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='AWS1')
channel.confirm_delivery()
channe2 = connection.channel()
channe2.queue_declare(queue='AWS2')
channe2.confirm_delivery()
for i 
channel.basic_publish(exchange='', routing_key='AWS1', body=0,mandatory=True)
channe2.basic_publish(exchange='', routing_key='AWS1', body=1,mandatory=True)
        
