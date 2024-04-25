from celery import Celery


celery = Celery("tasks", broker="redis://localhost")
celery.broker_connection()


@celery.task
def writefile(files: list[bytes]):
    for i, file in enumerate(files):
        with open(f"app/files/{i}.exe", "wb") as fl:
            fl.write(file)
