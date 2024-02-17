from fastapi import APIRouter, Depends, HTTPException
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

# создание ендпоинтов + отработка ошибок с отправкой информации пользователю
# стоит придерживаться единой структуры ответа
# как в данном случае, в returne
# ендпоинт по хорошему должен оборачиваться в try/except
# ОДИНАКОВАЯ СТРУКТУРА ОТВЕТОВ - ЭТО ВАЖНО
@router.get("")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    # try:
        query = select(operation).where(operation.type == operation_type)
        result = await session.execute(query)
        pre_res = list(map(lambda x: x[0], result.all()))
        return {
            "status": "success",
            "data": pre_res,
            "details": None
        }

    # except ZeroDivisionError:
    #     # Передать конкретную ошибку разработчикам
    #     return {
    #         "status": "error",
    #         "data": None,
    #         "details": "Делишь на ноль, не надо так"
    #     }
    #
    # except Exception:
    #     # Передать любую ошибку разработчикам
    #     return {
    #         "status": "error",
    #         "data": None,
    #         "details": None
    #     }
    # можно также подбирать ошибки с помощью рейзов, но мне верхний способ больше понравился
    # except Exception:
    #     # Передать ошибку разработчикам
    #     raise HTTPException(status_code=500, detail={
    #         "status": "error",
    #         "data": None,
    #         "details": None
    #     })




# Вот тут пример того как постить данные с помощью schemas
@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}