FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]


# ================= HOW TO RUN =================
# 1. Build Docker Image
# docker build -t insure-me .

# 2. Run Container
# docker run -d -p 5000:5000 insure-me

# 3. Open Browser
# http://localhost:5000