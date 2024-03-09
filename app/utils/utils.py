from enum import Enum


class StateBook(Enum):
    ASSET = 'Asset'   #ACTIVO
    IDLE = 'Idle'     #INACTIVO
    BORROWED = 'Borrowed'   #PRESTADO
