from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.core.container import Container
from app.routers.user_routers import router as user_router
from app.routers.payment_type_routers import payment_type_router

app = FastAPI()


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def root():
    return RedirectResponse(url='/docs')


class AppCreator:
    def __init__(self):
        self.app = FastAPI(
            title="Controle de Debitos",
            version='0.0.1',
        )

        self.container = Container()
        self.db = self.container.database()
        self.db.create_database()

        self.app.include_router(user_router)
        self.app.include_router(payment_type_router)


app_creator = AppCreator()
app = app_creator.app
