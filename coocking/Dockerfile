FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install -y \
	ca-certificates \
	python3-all-dev \
	python3-venv \
	postgresql-server-dev-all\
	build-essential
RUN python3 -m venv /env
ENV PATH="/env/bin/:$PATH"
WORKDIR /app
COPY . /app
RUN pip install -U pip wheel
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver"]
ENV PYTHONUNBUFFERED 1
