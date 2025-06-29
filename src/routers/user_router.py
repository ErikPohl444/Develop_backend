from src.models.user import User
from src.services.user_service import create_user_service, read_user_service, read_all_users_service
from src.services.db_service import SessionDep
from src.routers.generic_router_factory import create_crud_router


router = create_crud_router(
    model=User,
    create_service=create_user_service,
    read_service=read_user_service,
    read_all_service=read_all_users_service,
    resource_name="users",
    session_dep=SessionDep,
)
