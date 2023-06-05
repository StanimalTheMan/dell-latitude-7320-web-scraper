FROM python:3.9

ADD latitude_scraper.py .

RUN pip install requests beautifulsoup4

CMD ["python", "latitude_scraper.py"]