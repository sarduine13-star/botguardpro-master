from fastapi import APIRouter
router=APIRouter()
@router.post('/stripe/webhook')
async def wh():return {'received':True}