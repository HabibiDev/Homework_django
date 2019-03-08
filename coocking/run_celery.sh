sleep 10
su -m gavnuk -c "sudo celery -A coocking worker -l info"
su -m gavnuk -c "sudo celery -A coocking beat -l info"
