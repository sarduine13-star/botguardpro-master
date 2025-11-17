from fastapi import APIRouter
router=APIRouter()
@router.get('/raina/desktop')
async def r():return {'raina':'desktop ok'}