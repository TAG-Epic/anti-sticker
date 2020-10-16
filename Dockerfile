FROM python:3.8
WORKDIR bot/
RUN pip install speedcord==0.1.83
COPY main.py ./
CMD ["python", "main.py"]
