

build jenkins container:
docker build -t myjenkins-blueocean:2.346.1-1 ./jenkins/

run jenkins container:
docker run --name jenkins-blueocean --restart=on-failure --detach --network jenkins -v //var/run/docker.sock:/var/run/docker.sock --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.346.1-1
