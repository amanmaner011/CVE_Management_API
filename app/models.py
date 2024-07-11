from app import db

class CVE(db.Model):

    __tablename__ = 'cves'
    
    cve_id = db.Column(db.String, primary_key=True)
    severity = db.Column(db.String)
    cvss = db.Column(db.Float)
    affected_packages = db.Column(db.String)
    description = db.Column(db.String)
    cwe_id = db.Column(db.String)
