FROM nginx:alpine

WORKDIR /usr/share/nginx/html


COPY index.html .
COPY app.js .
COPY style.css .


COPY nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

#Removed the multi-stage build, as the retro team decided it wasn't needed.