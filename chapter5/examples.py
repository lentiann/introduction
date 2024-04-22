# easy, medium, hard
# import enum
from enum import Enum
from dataclasses import dataclass
import time

# class Level(Enum):
#     EASY = "EASY"
#     MEDIUM = "MEDIUM"
#     HARD = "MEDIUM"


# level = Level.EASY

# if level == Level.EASY:
#     print("You selected easy level")

# elif level == Level.MEDIUM:
#     print("You selected medium level")


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class Task:
    name: str
    priority: Priority


def measure_time(func):
    def wrapper(*args, **kwargs):
        print("Measure time")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result

    return wrapper


@measure_time
def complete_task(task: Task):
    print(f"Completing task {task.name}")
    time.sleep(1)


if __name__ == "__main__":
    tasks = [
        Task("Task 1", Priority.LOW),
        Task("Task 2", Priority.MEDIUM),
        Task("Task 3", Priority.HIGH),
    ]
    
    for task in tasks:
        complete_task(task)

    print("All tasks completed!")