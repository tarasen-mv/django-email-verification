import logging

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse

from webapp import celery_app


@celery_app.task
def send_verification_email(user_id):
	UserModel = get_user_model()
	try:
		user = UserModel.objects.get(pk=user_id)
		send_mail(
			'Verify your account',
			'Follow this link to verify your account: http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
			'from@quickpublisher.dev',
			[user.email],
			fail_silently=False,
		)
	except UserModel.DoesNotExist:
		logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)
