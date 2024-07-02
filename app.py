from flask import Flask, request, jsonify
from models import db, ExampleNames
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/add', methods=['POST'])
def add_example_name():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    try:
        new_example_name = ExampleNames(name=data['name'])
        db.session.add(new_example_name)
        db.session.commit()
        return jsonify({'message': 'Record added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/search', methods=['GET'])
def search_example_names():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name parameter is required'}), 400
    try:
        results = ExampleNames.query.filter(ExampleNames.name.ilike(f'%{name}%')).all()
        if not results:
            return jsonify({'message': 'No records found'}), 404
        return jsonify([result.to_dict() for result in results]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
