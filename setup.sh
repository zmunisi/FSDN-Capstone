# Database PATH
export SQLALCHEMY_DATABASE_URI='postgresql://zmunisi:@localhost:5432/capstone'
export SQLALCHEMY_DATABASE_URI='postgresql://{{username}}:@localhost:5432/{{database_name}}'
export SQLALCHEMY_TRACK_MODIFICATIONS=False
export EXCITED=true

# Flask App config
export FLASK_APP=app
export FLASK_ENV=development

# Pagination
export RESULTS_PER_PAGE=10

# Auth0
export AUTH0_DOMAIN='zmunisi.eu.auth0.com'
export ALGORITHMS='RS256'
export API_AUDIENCE='capstone'