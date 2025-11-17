from fastapi import APIRouter
router=APIRouter()
@router.get('/raina/background')
async def r():return {'raina':'background ok'}