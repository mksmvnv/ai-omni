from sqlalchemy import Integer, BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from db.engine import BaseModel


class Calculate(BaseModel):
    __tablename__ = "calculate_tokens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    user_name: Mapped[str] = mapped_column(String)
    user_tokens: Mapped[int] = mapped_column(Integer)
    ai_tokens: Mapped[int] = mapped_column(Integer)
