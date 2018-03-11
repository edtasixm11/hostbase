docker build -t <imatge> .
docker run --rm --name h1 -h h1 -p 7:7 -p 9:9 -p 13:13 -p 19:19 -p 20-21:20-21  -p23:23 -p 25:25 -p 37:37 -p 69:69 -p 80:80 -p 110:110 -p 143:143 -p 993:993 -p 995:995  -p 2007:2007 -p 2013:2013 -p 2080:2080  -p 50001:50001 -d <imatge>
#pendent: -p 22:22

docker swarm init
docker stack deploy -c docker-compose.yml mylab
docker service ls
docker service ps mylab
docker container ls -q
docker stack rm mylab
docker swarm leave --force

