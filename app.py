from flask import Flask, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import BadRequest
from pydantic import ValidationError

from db import session_factory
from models import ExampleNames
from schemas import ExampleNamesVal


app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add_record():
    try:
        try:
            data = request.get_json()
        except BadRequest:
            return jsonify({"error": "Invalid JSON format"}), 400

        try:
            record = ExampleNamesVal(**data)
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

        session = session_factory()
        new_record = ExampleNames(name=record.name)
        session.add(new_record)
        session.commit()
        return jsonify({"message": "Record added successfully"}), 201
    except KeyError:
        return jsonify({"error": "Invalid JSON format or missing fields"}), 400
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


@app.route('/search', methods=['GET'])
def search_records():
    try:
        name = request.args.get('name')
        if not name:
            return jsonify({"error": "Name parameter is required"}), 400

        session = session_factory()
        results = session.query(ExampleNames).filter(ExampleNames.name == name).all()
        if not results:
            return jsonify({"message": "No records found"}), 404

        return jsonify([record.to_dict() for record in results]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
