from celery import Celery

app = Celery(
    "shop_app.celery_app",
    broker="amqp://guest:guest@192.168.0.104:5672//",
    backend="rpc://",
    include=["shop_app.tasks"],
    broker_connection_retry_on_startup=True,
)
