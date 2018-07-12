FROM        hsj2334p1/eb-docker:base
MAINTAINER  devhsj@gmail.com


ENV         BUILD_MODE              production
ENV         DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

RUN         rm -rf /srv/ticket
COPY        . /srv/ticket

#Nginx 설정파일 복사 및 링크
RUN         cp -f   /srv/ticket/.config/${BUILD_MODE}/nginx.conf       /etc/nginx/nginx.conf &&\
            cp -f   /srv/ticket/.config/${BUILD_MODE}/nginx-app.conf   /etc/nginx/sites-available/ &&\
            rm -f   /etc/nginx/sites-enabled/* &&\
            ln -sf  /etc/nginx/sites-available/nginx-app.conf   /etc/nginx/sites-enabled/
RUN         mkdir
#supervisord 설정 파일 복사
RUN         cp -f   /srv/ticket/.config/${BUILD_MODE}/supervisord.conf /etc/supervisor/conf.d/
RUN         mkdir /var/log/redis
WORKDIR    /srv/project/app

#supervisor를 실행
CMD         pkill nginx; supervisord -n
EXPOSE      80