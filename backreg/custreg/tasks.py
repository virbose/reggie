from __future__ import absolute_import, unicode_literals
import logging
import requests

from django.conf import settings
from backreg.celery_worker import app
from .models import CustomerPlan

logger = logging.getLogger("celery")

class RequestException(Exception):
    pass


@app.task(autoretry_for=(RequestException,), retry_kwargs={'max_retries': 10}, retry_backoff=True)
def get_plans_for_new_user(user_id, country_code) -> None:
    """
    Make a request to the external API
    If we get a good response, carry on with processing
    If not, raise a RequestException which will cause the app to run again
    """
    url = settings.EXTERNAL_API_URL.format(iso2_code=country_code)
    response = requests.get(url)
    if response.ok:
        data = response.json().get('data')
        for plan in data:
            if plan.get('active'):
                CustomerPlan.objects.create(
                    customer_id=user_id,
                    name=plan.get('plan'),
                    billing_interval=plan.get('billing_interval'),
                    frequency=plan.get('frequency'),
                    currency=plan.get('currency')
                )
    else:
        raise RequestException("Request Failed with code ", response.status_code)
