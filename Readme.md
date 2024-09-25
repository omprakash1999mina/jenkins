# Starts with
- Vm + jenkins 
- Docker jenkins

## Docker jenkins
- pull the jenkins image from docker-hub
``` 
docker pull jenkins/jenkins 
```
- run docker shell as root user
``` 
docker exec -it --user root <container_name_or_id> /bin/bash
```

