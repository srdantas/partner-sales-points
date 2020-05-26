# Partner sales points
Usage for the register, find and search partners based on GEOJson with MongoDB.

### Requirements
- python3.8
- docker

## Build a docker image
for build, run this command:
```shell script
sudo docker build -t partner-sales-points .
```

for run that:
```shell script
sudo docker run -p 5000:5000 partner-sales-points
```

When you like local run the app, you can run this:
```shell script
pip install . && flask run
```