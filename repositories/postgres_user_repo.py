import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Optional
from models.user import User
from repositories.base import UserRepository
from config import DATABASE_URL

class PostgresUserRepository(UserRepository):
    def _get_connection(self):
        return psycopg2.connect(DATABASE_URL)

    def create_user(self, name: str, email: str) -> User:
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id, created_at",
                    (name, email)
                )
                row = cur.fetchone()
                return User(id=row["id"], name=name, email=email, created_at=row["created_at"])

    def get_user_by_email(self, email: str) -> Optional[User]:
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                row = cur.fetchone()
                return User(**row) if row else None

    def get_all_users(self) -> List[User]:
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM users ORDER BY id")
                rows = cur.fetchall()
                return [User(**r) for r in rows]
