FROM django:onbuild

WORKDIR /CBS

COPY ..

RUN pip install -r requirements.txt

CMD ["python", "manage.py"]

