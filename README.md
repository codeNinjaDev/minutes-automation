# minutes-automation
Help me to automate taking minutes for 4-H meeting. Generates a pdf with LaTeX
## Docker set-up
### Build dockerfile
```docker build -t secretary .```
### Run docker with shared drive
```docker run -v <hostpath>:/home/ -it secretary```
