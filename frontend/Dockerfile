FROM node:lts-alpine3.17 as builder

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install -g pnpm

RUN pnpm install

COPY . .

RUN npm run build

CMD ["http-server", "dist"]

FROM nginx:1.23.4 as production-build

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/dist /usr/share/nginx/html
COPY --from=builder /app/src/assets /usr/share/nginx/html/assets

ENTRYPOINT ["nginx", "-g", "daemon off;"]
