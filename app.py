import os
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from models import setup_db, Actors, Movies


def paginate_results(request, selection):
    results_per_page = os.environ['RESULTS_PER_PAGE']
    results_per_page = int(results_per_page)
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * results_per_page
    end = start + results_per_page

    results = [result.format() for result in selection]
    current_selection = results[start:end]

    return current_selection


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

# ROUTES
    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello"
        if excited == 'true':
            greeting = greeting + " HEROKU!!!!!"
        return jsonify(greeting)

    # List Actors
    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actors.query.order_by(Actors.id).all()

        if len(actors) == 0:
            abort(404)

        results = paginate_results(request, actors)
        return jsonify({
            'success': True,
            'actors': results
        })

    # Add Actors
    @app.route('/actors', methods=['POST'])
    def add_actor():
        body = request.get_json()

        if not ('name' in body and 'surname' in body and 'age'
                in body and 'gender' in body):
            abort(400)

        new_name = body.get('name', None)
        new_surname = body.get('surname', None)
        new_age = int(body.get('age', None))
        new_gender = body.get('gender', None)

        try:
            int(body.get('age'))
        except Exception:
            abort(400)

        try:
            actor = Actors(
                        name=new_name,
                        surname=new_surname,
                        age=new_age,
                        gender=new_gender
                        )

            actor.insert()

            return jsonify({
              'success': True,
              'created': actor.id
            })
        except Exception:
            abort(422)

    # Update Actors
    @app.route('/actors/<int:id>', methods=['PATCH'])
    def update_actor(id):
        actor = Actors.query.get(id)

        if actor is None:
            abort(404)

        body = request.get_json()

        if 'name' in body:
            if body.get('name') is None:
                abort(400)

            actor.name = body.get('name', None)

        if 'surname' in body:
            if body.get('surname') is None:
                abort(400)

            actor.surname = body.get('surname', None)

        if 'age' in body:
            try:
                int(body.get('age'))
            except Exception:
                abort(400)

            if body.get('age') is None:
                abort(400)

            actor.age = int(body.get('age'))

        if 'gender' in body:
            if body.get('gender') is None:
                abort(400)

            actor.gender = body.get('gender', None)

        try:

            actor.update()

            return jsonify({
              'success': True,
              'updated': actor.id
            })
        except Exception:
            abort(422)

    # Delete Actors
    @app.route('/actors/<int:id>', methods=['DELETE'])
    def delete_actor(id):
        actor = Actors.query.get(id)

        if actor is None:
            abort(422)

        try:
            actor.delete()
        except Exception:
            abort(422)

        return jsonify({
              'success': True,
              'deleted': id
            })

    # List Movies
    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = Movies.query.order_by(Movies.id).all()

        if len(movies) == 0:
            abort(404)

        results = paginate_results(request, movies)
        return jsonify({
            'success': True,
            'actors': results
        })

    # Add Movie
    @app.route('/movies', methods=['POST'])
    def add_movie():
        body = request.get_json()

        if not ('title' in body and 'director' in body and 'desc'
                in body and 'release_date' in body):
            abort(400)

        new_title = body.get('title', None)
        new_director = body.get('director', None)
        new_desc = body.get('desc', None)
        new_release_date = body.get('release_date', None)

        print(new_title)
        print(new_director)
        print(new_desc)
        print(new_release_date)

        try:
            movie = Movies(
                        title=new_title,
                        director=new_director,
                        desc=new_desc,
                        release_date=new_release_date
                        )

            movie.insert()

            return jsonify({
              'success': True,
              'created': movie.id
            })
        except Exception:
            abort(422)

    # Update Movie
    @app.route('/movies/<int:id>', methods=['PATCH'])
    def update_movie(id):
        movie = Movies.query.get(id)

        if movie is None:
            abort(404)

        body = request.get_json()

        if 'title' in body:
            if body.get('title') is None:
                abort(400)

            movie.title = body.get('title', None)

        if 'director' in body:
            if body.get('director') is None:
                abort(400)

            movie.director = body.get('director', None)

        if 'desc' in body:
            if body.get('desc') is None:
                abort(400)

            movie.desc = body.get('desc')

        if 'release_date' in body:
            if body.get('release_date') is None:
                abort(400)

            movie.release_date = body.get('release_date', None)

        try:

            movie.update()

            return jsonify({
              'success': True,
              'updated': movie.id
            })
        except Exception:
            abort(422)

    # Delete Movie
    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_movie(id):
        movie = Movies.query.get(id)

        if movie is None:
            abort(422)

        try:
            movie.delete()
        except Exception:
            abort(422)

        return jsonify({
              'success': True,
              'deleted': id
            })

    # ERROR HANDLERS
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
          "success": False,
          "error": 400,
          "message": "bad request"
        }), 400

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
          "success": False,
          "error": 500,
          "message": "internal server error"
        }), 500

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized'
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'Forbidden'
        }), 403

    # RETURN APP
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
