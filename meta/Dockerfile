FROM python:3.9

COPY meta/requirements.txt requirements.txt
RUN python3 -m pip install --default-timeout=100 --upgrade pip && python3 -m pip install --default-timeout=100 -r requirements.txt

COPY meta meta

RUN chmod +x meta/main.py
RUN chmod +x meta/run.sh


ENTRYPOINT [ "python3", "meta/main.py" ]