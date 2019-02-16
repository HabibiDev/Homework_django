from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .models import Order

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="task_deactivate_old_order",
    ignore_result=True
)
def task_deactivate_old_order():
	orders = Order.objects.all()
	for order in orders:
		if order.is_active:
			order.is_active = False
			order.save()
			logger.info('order:{0} deactivated'.format(order.id))



