from flask import request, jsonify
from app import app, db
from app.models import CVE

@app.route('/')
def home():
    return 'SecOps Solution CVE API'

@app.route('/cve/<cve_id>', methods=['GET'])
def get_cve(cve_id):
    cve = CVE.query.get(cve_id)
    if cve is None:
        return jsonify({'error': 'CVE not found'}), 404
    return jsonify({
        'cve_id': cve.cve_id,
        'severity': cve.severity,
        'cvss': cve.cvss,
        'affected_packages': cve.affected_packages,
        'description': cve.description,
        'cwe_id': cve.cwe_id
    })

@app.route('/cve/all', methods=['GET'])
def get_all_cves():
    cves = CVE.query.all()
    return jsonify([{
        'cve_id': cve.cve_id,
        'severity': cve.severity,
        'cvss': cve.cvss,
        'affected_packages': cve.affected_packages,
        'description': cve.description,
        'cwe_id': cve.cwe_id
    } for cve in cves])

@app.route('/cve/addCVE', methods=['POST'])
def add_cve():
    data = request.get_json()
    cve = CVE(**data)
    db.session.add(cve)
    db.session.commit()
    return jsonify({'message': 'CVE added successfully'}), 201

@app.route('/cve/<cve_id>', methods=['DELETE'])
def delete_cve(cve_id):
    cve = CVE.query.get(cve_id)
    if cve is None:
        return jsonify({'error': 'CVE not found'}), 404
    db.session.delete(cve)
    db.session.commit()
    return jsonify({'message': 'CVE deleted successfully'}), 200

@app.route('/cve/<cve_id>', methods=['PUT'])
def update_cve(cve_id):
    cve = CVE.query.get(cve_id)
    if cve is None:
        return jsonify({'error': 'CVE not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(cve, key, value)
    db.session.commit()
    return jsonify({'message': 'CVE updated successfully'}), 200
