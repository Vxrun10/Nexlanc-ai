

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = "mysql+pymysql://3fJbKsdTZJN4psR.root:P4rWNqS9tDrBr5vm@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?ssl_ca=<CA_PATH>&ssl_verify_cert=true&ssl_verify_identity=true"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": "C:/projects/Nexlanc Ai/ca.pem"   
        }
    }
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()