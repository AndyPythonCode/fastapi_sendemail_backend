from manage import CONEXION
import sqlalchemy

email = sqlalchemy.Table(
    "email",
    CONEXION.getMetaData(),
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(80)),
    sqlalchemy.Column("email", sqlalchemy.String(80)),
    sqlalchemy.Column("message", sqlalchemy.Text)
)