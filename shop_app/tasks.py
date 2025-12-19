import logging
from time import sleep
from shop_app.celery_app import app
from shop_app.smtp_email_backend import SmtpEmailBackend

log = logging.getLogger(__name__)


def fetch_users_info(
    user_ids: list[int],
) -> list[tuple[str, str]]:
    return [
        (
            f"User #{user_id:02d}",
            f"email.user{user_id:02d}@example.com",
        )
        for user_id in user_ids
    ]


newsletter_body_template = """\
Dear {name},

Our sale just started!
Sale #{sale_id}
Use our promocode: "{promo}"!
"""


@app.task
def send_email_newsletter(
    user_ids: list[int],
    sale_id: int,
    promo_code: str,
):
    log.info(
        "Start sending newsletter #%s email to %s users",
        sale_id,
        len(user_ids),
    )

    email_backend = SmtpEmailBackend(
        smtp_server="192.168.0.104",
        smtp_port=1025,
        from_email="noreply@shop.com",
    )

    users_info = fetch_users_info(user_ids)

    for name, email in users_info:
        subject = f"{name}, join our sale #{sale_id}!"
        body = newsletter_body_template.format(
            name=name,
            sale_id=sale_id,
            promo=promo_code,
        )

        email_backend.send_email(
            recipient=email,
            subject=subject,
            body=body,
        )
        log.info("Sent email to user %s", email)
        sleep(1)

    log.info(
        "Finished sending newsletter #%s email to %s users",
        sale_id,
        len(user_ids),
    )
