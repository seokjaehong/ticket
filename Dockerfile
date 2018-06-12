FROM        hsj2334p1/eb-docker:base
MAINTAINER  devhsj@gmail.com


ENV         BUILD_MODE              production
ENV         DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

COPY        . /srv/ticket
#Nginx 설정파일 복사 및 링크

RUN         cp -f   /srv/ticket/.config/${BUILD_MODE}/nginx.conf       /etc/nginx/nginx.conf &&\
            cp -f   /srv/ticket/.config/${BUILD_MODE}/nginx-app.conf   /etc/nginx/sites-available/ &&\
            rm -f   /etc/nginx/sites-enabled/* &&\
            ln -sf  /etc/nginx/sites-available/nginx-app.conf   /etc/nginx/sites-enabled/\
            cp -f   /srv/ticket/app/cronjob.txt /etc/cron.d/
# crontab 실행 
RUN         crontab /etc/cronjob.txt
RUN         chmod 600 /etc/crontab

#supervisord 설정 파일 복사
RUN         cp -f   /srv/ticket/.config/${BUILD_MODE}/supervisord.conf /etc/supervisor/conf.d/

#supervisor를 실행
CMD         pkill nginx; supervisord -n
EXPOSE      80