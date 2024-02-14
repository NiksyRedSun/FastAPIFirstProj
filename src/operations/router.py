from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.operations.schemas import OperationCreate
from src.database import get_async_session
from src.operations.models import operation
# from operations.schemas import OperationCreate


# Создание дополнительного пути
router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

# создание ендпоинтов
@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.с.type == operation_type)
    result = await session.execute(query)
    return result.mappings().all()



# Вот тут пример того как постить данные с помощью schemas
@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}