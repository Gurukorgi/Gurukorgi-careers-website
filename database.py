from sqlalchemy import create_engine, text
import os
my_secret = os.environ['DB_CONNECTION_STRING']
db_connection_string = my_secret

engine = create_engine(db_connection_string, connect_args={'ssl': {'ssl_ca': '/etc/ssl/cert.pem'}})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.fetchall():
        jobs.append(dict(row._asdict()))
    return jobs

# def load_job_from_db(id):
#   with engine.connect() as conn:
#     result = conn.execute(
#       text('SELECT * FROM jobs WHERE id = :val'),val=id
#     )
#     rows = result.all()
#     if len(rows) == 0:
#       return None
#     else:
#       return dict(rows[0])

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text('SELECT * FROM jobs WHERE id = :id'),
            {"id": id},
        )
        row = result.fetchone()
        if row is None:
            return None
        else:
            job = dict(zip(result.keys(), row))
            return job


















