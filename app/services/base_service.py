from typing import Type

from app.repository.base_repository import BaseRepository
from app.schema.base_schema import BaseSchema


class BaseService:
    def __init__(self, repository: BaseRepository) -> None:
        self.repository = repository

    def get_list(self, skip: int = 0, limit: int = 10):
        return self.repository.read_list(skip, limit)

    def get_by_id(self, id: int):
        return self.repository.read_by_id(id)

    def add(self, schema: Type[BaseSchema]):
        return self.repository.create(schema)

    def patch(self, id: int, schema: Type[BaseSchema]):
        return self.repository.update(id, schema)

    def patch_attr(self, id: int, column: str, value):
        return self.repository.update_attr(id, column, value)

    def remove_by_id(self, id: int):
        return self.repository.delete_by_id(id)
