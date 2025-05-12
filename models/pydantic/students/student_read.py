from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class StudentReadModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    student_id: int = Field(alias="id")
    name: str
    birth_date: date
    course_name: str | None = None
    photo_url: str | None



    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))