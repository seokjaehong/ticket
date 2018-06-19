# Flight ticket Alarm service
## 1. Introduction
Flight ticket price changes everyday. For checking, you have to access the site everyday. 

This is a service provides airline ticket alarm. 

Don't waste your time and resource,just select the date and price what you want and write an email.

(v.0.1) GMP -CJU (Tway airline(https://www.twayair.com/main.do#;))

## 2. How to use 
1. select date or month, price, and an email.
2. If flight ticket price go down under your choice, you can get notice.
3. Data Crawling Cycle
    - every 6 hours for 3 months data
    - 
## 3. Configuration
- Language
    - Python/Django
    - Docker
    - PostgreSQL
    - AWS EC2/RDS/S3/Elastic Beanstalk
    - Sentry
    - nginx/uwsgi
    - 
- Contents
    - Seperate Enviroments(local/dev/production)
    - `.secrets key` manage
    - cronjob with uwsgi
## 4. Requirements
raven<6.7
uWSGI<2.1
boto3<1.7
Django<2.1
django-storages==1.6.5
Pillow<6.0.0
psycopg2-binary==2.7.4
selenium==3.12.0

## 5. AWS environment
- Python(3.6)
- S3 Bucket, AWS AccessKey, SecretAccessKey for IAM User
- RDS Database(need add security group), RDS User, pwd

## 6.Installation(Django runserver)
```
pip install -r .requirements/dev.txt
```

### Local environment
```
pip install -r .requirements/dev.txt
python manage.py runserver --settings=config.settings.local 
```
### Dev environment
```
pip install -r .requirements/dev.txt
python manage.py runserver --settings=config.settings.dev
```
### Production environment (deploy)
```
pip install -r .requirements/production.txt
python manage.py runserver --settings=config.settings.production
```

## 7.Installation(Docker)
### Dockerfile.base 
```
install and setting pyenv 3.6.4, zsh, chromedriver=2.39 for selenium
```
### Dockerfile 

```
docker build -t eb-docker:base -f Dockerfile.base .
docker tag eb-docker:base <Username>/<dockerhubName>:base
docker push <Username>/<DockerhubName>:base
```

```
docker build -t eb-docker -f Dockerfile .
```

## ETC
### .config 
```
cronjob 
```
### Secrets
`.secrets/base.json`
```json
"SECRET_KEY": "<Django settings SECRET_KEY value>"
  "RAVEN_CONFIG": {
    "dsn": "https://<sentry_Client_Keys>",
    "release": "raven.fetch_git_sha(os.path.abspath(os.pardir))"
  },
  "SUPERUSER_USERNAME":"<superuser username>",
  "SUPERUSER_PASSWORD":"<superuser user-password>",
  "SUPERUSER_EMAIL":"<superuser user-email>",
  "AWS_ACCESS_KEY_ID":"<AWS_ACCESS_KEY value> ",
  "AWS_SECRET_ACCESS_KEY":"<AWS_SECRET_ACCESS_KEY value>",
  "AWS_STORAGE_BUCKET_NAME":"<AWS_BUCKET_NAME>",
  "AWS_S3_REGION_NAME":"<region name>, default='ap-northeast-2'",
  "AWS_S3_SIGNATURE_VERSION":"<version>, default: s3v4",
  "AWS_DEFAULT_ACL":"private",
```
`.secrets/dev.json & .secrets/production.json`
```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "<RDS ADDRESS. ex)instance-name.###.region.rds.amazonaws.com>",
      "NAME": "<DB name>",
      "USER": "<DB username>",
      "PASSWORD": "<DB user password>",
      "PORT": <Port number, default:5432>
    }
  }
}
```
