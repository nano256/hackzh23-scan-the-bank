FROM python:3.11
COPY app /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# CMD ["sh", "eval.sh"]
CMD ["python", "crawler.py"]