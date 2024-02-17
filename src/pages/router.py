from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.operations.router import get_specific_operations

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

# подключаем джинджу, указываем директорию с шаблонами
templates = Jinja2Templates(directory="src/templates")


# реквест нужно получить и передать в шаблон, в дальнейшем из него можно будет вытаскивать какие-нибудь переменные
@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


# обрати внимание на то, как получаем операции с помощью депендс
@router.get("/search/{operation_type}")
def get_search_page(request: Request, operations=Depends(get_specific_operations)):
    # обрати внимание и на то, что из операций вытаскиваем только дату
    # print(operations["data"][0])
    return templates.TemplateResponse("search.html", {"request": request, "operations": operations["data"]})