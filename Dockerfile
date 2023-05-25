FROM python:3.11

WORKDIR /usr/app

COPY Pipfile Pipfile.lock ./
RUN pip3 install pipenv
RUN pipenv requirements > requirements.txt
RUN pip3 install -r requirements.txt

COPY main.py main.py

ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]