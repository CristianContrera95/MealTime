from backend_test.celery import app as app_celery


@app_celery.task(name='test')
def meal_delivery_test() -> None:
    print('Test celery app')
