from django.conf import settings
from django.core.mail import send_mail


def send_email(title, message, sender, email):
    return send_mail(title,
                     message,
                     [sender],
                     ['{0}'.format(email)]
                     )


def send_order_verification(order_detail):
    return send_mail(
                    ('Tidlundsved.se - Tack för din order #{0}'.format(order_detail.pk)),
                    ('Namn: {0}\nE-post: {1}\nTelefonnummer: {2}\nVal: {3} med {4}'.format(
                        order_detail.name,
                        order_detail.email,
                        order_detail.phone_number,
                        order_detail.product_type,
                        order_detail.firewood_choice) +
                        '\nKvantitet: {0}\nVal av leverans: {1}\nLeveransadress: {2}'.format(
                        order_detail.quantity,
                        order_detail.delivery_option,
                        order_detail.delivery_address) +
                        '\nÖvrig info: {0}\nBetala med: {1}'.format(
                        order_detail.description,
                        order_detail.payment_method),
                        '\n\nVid frågor om din order, ta kontakt med oss på mail: andtidlund@hotmail.com' +
                        ' eller telefon: 070-585 43 38‬' +
                        '\n\nhttps://www.tidlundsved.se'
                     ),
                     [settings.EMAIL_SEND_FROM],
                     [order_detail.email, settings.EMAIL_SEND_TO]
                     )
