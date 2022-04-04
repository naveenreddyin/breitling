# How to run?
* `docker-compose up -d`, frontend is available at `http://localhost:3000` if docker-compose ran succesfully. 

# How to run backend tests?
* Create virtual env
* Install requirements using `pip install -r requirements.txt` from backend folder or use `docker-compose exec`
* Run, `py.test -svv` or `docker-compose exec backend py.text -svv`

# How to do e2e using Cypress for frontend?
* `yarn cypress open` from frontend folder after doing `yarn install` 