# Database PATH
export SQLALCHEMY_DATABASE_URI='postgresql://zmunisi:@localhost:5432/capstone'
export SQLALCHEMY_TRACK_MODIFICATIONS=False

# Flask App config
export FLASK_APP=app
export FLASK_ENV=development

# Heroku
export HEROKU_HOST='https://fsnd-capstone-zmunisi.herokuapp.com/'

# Pagination
export QUESTIONS_PER_PAGE=10