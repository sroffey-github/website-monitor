
# Website Monitor

A simple website monitoring application using python3 and flask

## Installation

Clone site-list with git

```bash
  git clone https://github.com/sroffey-github/website-monitor.git
  cd website-monitor/web-app
  mv .env.example .env
```
you will then need to add the path of your db folder followed by /info.db to your .env file

To run this with docker (edit the run.sh file accordingly):
```bash
  chmod +x run.sh
  ./run.sh
```
    
## Authors

- [@sroffey-github](https://www.github.com/sroffey-github)


## Folder Structure

```
website-monitor/
├─ sh/
│  ├─ monitor.sh
│  ├─ monitor.py
│  ├─ run.sh
├─ web-app/
│  ├─ db/
│  │  ├─ info.db
│  ├─ templates/
│  │  ├─ index.html
│  ├─ .env.example
│  ├─ app.py
│  ├─ Dockerfile
│  ├─ requirements.txt
│  ├─ run.sh
.gitignore
```

