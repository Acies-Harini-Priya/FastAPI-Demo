from fastapi import APIRouter

from dev.services.InternsInfoService import InternsInfoService

interns_info_router = APIRouter(
    prefix="/InternsInfo",
)

@interns_info_router.get("/GetInternsDetails")
async def getInternsDetails():
    response_code, response_data = InternsInfoService.getInternsDetails()
    return {"response_code": response_code, "response_data":response_data}

