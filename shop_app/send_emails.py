import random
import string

from shop_app.tasks import send_email_newsletter


def fetch_users_ids_for_newsletter():
    return [random.randint(1, 100) for _ in range(random.randint(20, 50))]


def send_newsletters_task():
    user_ids = fetch_users_ids_for_newsletter()
    promo_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
    task = send_email_newsletter.delay(
        user_ids=user_ids,
        promo_code=promo_code,
        sale_id=random.randint(50, 200),
    )
    print("sent task", task, repr(task))
