from fastapi import APIRouter

router = APIRouter(tags=["Home"])


@router.get("/")
def get_application_status():
    return {
        "status": "success",
        "application": "AI Placement Preparation Agent",
        "version": "1.0.0"
    }