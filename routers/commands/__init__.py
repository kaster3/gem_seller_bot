__all__ = ("router",)

from aiogram import Router

from .base_commands import router as base_commands_router

router = Router(name=__name__)

for r in (base_commands_router,):
    router.include_router(
        router=r,
    )
