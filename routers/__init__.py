__all__ = ("router",)

from aiogram import Router

from .commands import router as commands_router
from .survey import router as survey_router

router = Router(name=__name__)

for r in (commands_router, survey_router):
    router.include_router(
        router=r,
    )
