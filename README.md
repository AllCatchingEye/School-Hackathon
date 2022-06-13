# School Hackathon
Software Architektur SoSe 22 x MUC.DAI \
\
**Product Owner:**\
Lionel Wisskirchen <a href="MAILTO:lionel.wisskirchen@hm.edu"><lionel.wisskirchen@hm.edu></a> \
**Team Member:**\
Vu Le <a href="MAILTO:vu.le@hm.edu"><vu.le@hm.edu></a> \
Merlin Reiter <a href="MAILTO:m.reiter@hm.edu"><m.reiter@hm.edu></a> \
Marius Thoma <a href="MAILTO:mthoma@hm.edu">mthoma@hm.edu</a> \
Georg Lang <a href="MAILTO:glang@hm.edu"><glang@hm.edu></a> \
Anton Stimmer <a href="MAILTO:stimmer.anton@hm.edu">stimmer.anton@hm.edu</a>

# Prototype
## Prototype Requirements 

- Install https://www.docker.com
- Install https://docs.docker.com/compose/
- Clone Project

## Starting Prototype
- Switch to prototype folder
- Build Images `docker-compose build .`

### Start in Development Mode
- Start Protoype `docker-compose up` 
- Go to `http://localhost:80`
- If npm packages are missing this can be fixed by an npm install in the frontend container.
  
### Starting Production Build
- Start Prototype `docker-compose -f docker-compose.yml -f docker-compose.production.yml up`  
- Go to `http://localhost:80`
