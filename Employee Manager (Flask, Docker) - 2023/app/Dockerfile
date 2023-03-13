FROM python:3.10.7

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY static /app/static
COPY templates /app/templates
COPY database.py /app
COPY dbModel.py /app
COPY employees.py /app
COPY jobs.py /app
COPY app.py /app
CMD python app.py