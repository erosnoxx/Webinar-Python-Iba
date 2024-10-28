from abc import ABC
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.TodoEntity import TodoEntity


class ITodoRepository(ABC, BaseRepository[TodoEntity]):
    pass
