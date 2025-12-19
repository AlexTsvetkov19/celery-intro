from celery.result import AsyncResult

from shop_app.celery_app import app


def main():
    result = AsyncResult(
        "4328910e-4827-4638-92c8-c88e2a804aa3",
        app=app,
    )
    print("result:", result)
    print("result.status:", result.status)
    print("result.name:", result.name)


if __name__ == "__main__":
    main()
