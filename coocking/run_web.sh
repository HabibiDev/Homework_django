sleep 10
su -m gavnuk -c "sudo python3 manage.py makemigrations"  
su -m gavnuk -c "sudo python3 manage.py migrate"
su -m gavnuk -c "sudo python3 manage.py createsuperuser --username admin --password admin --email 'admin@email.com'"
su -m gavnuk -c "sudo python3 manage.py runserver 0.0.0.0:8000"  