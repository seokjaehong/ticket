FROM        hsj2334p1/eb-docker:base
MAINTAINER  devhsj@gmail.com

COPY        . /srv/ticket
#Nginx 설정파일 복사 및 링크
RUN         cp -f /srv/ticket/.config/nginx.conf /etc/nginx/nginx.conf
RUN         cp -f /srv/ticket/.config/nginx-app.conf /etc/nginx/sites-available/
RUN         rm -f /etc/nginx/sites-enabled/*
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/

#supervisord 설정 파일 복사
RUN         cp /srv/ticket/.config/supervisord.conf /etc/supervisor/conf.d/
#supervisor를 실행
CMD         pkill nginx; supervisord -n
EXPOSE      80