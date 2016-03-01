# Cloudant parallel view query performance testing

## Requirements

`pip -r requirements.txt`

## Usage

```
$ export CLOUDANT_USERNAME=<username>
$ read -s CLOUDANT_PASSWORD
$ export CLOUDANT_PASSWORD
$ locust --host "https://physion-testy016.cloudant.com" --no-web -c 100 -n 1000 -r 100
```
