from datetime import datetime


class CreateTodoInputDto:
    def __init__(self, 
                title: str,
                status: str, 
                owner_name: str,
                description: str=None,
                due_date: datetime=None) -> None:
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.owner_name = owner_name
    
    def to_dict(self) -> dict[str, str]:
        return {
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'due_date': self.due_date,
            'owner_name': self.owner_name}
