from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Lese Umgebungsvariablen für die PostgreSQL-Verbindung
# Fallback-Werte sind gesetzt, falls Umgebungsvariablen nicht definiert sind
DB_USER = os.getenv("POSTGRES_USER", "root")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "root")
DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "db")

# Zusammensetzen der vollständigen Verbindungs-URL im PostgreSQL-Format
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Initialisiere SQLAlchemy Engine (stellt Verbindung zur Datenbank her)
engine = create_engine(DATABASE_URL)

# Erstelle eine Session-Klasse zur Verwaltung von Transaktionen
# autocommit=False: Änderungen müssen explizit gespeichert werden
# autoflush=False: kein automatisches Flush vor Queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Basisklasse für die ORM-Modelle – dient als Grundlage für alle Datenbanktabellen
Base = declarative_base()

