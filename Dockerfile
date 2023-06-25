FROM python:3.11.4
WORKDIR /myapp
COPY . .
RUN pip install -r requirements.txt
ENV MONGODB_URL=mongodb://0.0.0.0:27017/ \
    HOST=0.0.0.0 \
    IS_DEBUG_MODE=false

EXPOSE 8881

CMD ["python", "main.py"]