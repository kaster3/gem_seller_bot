__all__ = ("router",)

from aiogram import Router

from .handlers import router as survey_handlers_router

router = Router(name="survey")
router.include_router(router=survey_handlers_router)
