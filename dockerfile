FROM postgres
WORKDIR /home/
RUN apt-get --allow-releaseinfo-change update
COPY . requirements.txt
RUN pip install -r requirements.txt
COPY . .
