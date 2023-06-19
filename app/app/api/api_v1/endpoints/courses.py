from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Course])
def read_courses(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve course.
    """
    if crud.user.is_superuser(current_user):
        courses = crud.course.get_multi(db, skip=skip, limit=limit)
    else:
        courses = crud.course.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return courses


@router.post("/", response_model=schemas.course)
def create_course(
    *,
    db: Session = Depends(deps.get_db),
    course_in: schemas.CourseCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new course.
    """
    course = crud.course.create_with_owner(db=db, obj_in=course_in, user=current_user.id)
    return course


@router.put("/{id}", response_model=schemas.course)
def update_course(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    course_in: schemas.CourseUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an course.
    """
    course = crud.course.get(db=db, id=id)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    if not crud.user.is_superuser(current_user) and (course.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    course = crud.course.update(db=db, db_obj=course, obj_in=course_in)
    return course


@router.get("/{id}", response_model=schemas.course)
def read_course(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get course by ID.
    """
    course = crud.course.get(db=db, id=id)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    if not crud.user.is_superuser(current_user) and (course.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return course


@router.delete("/{id}", response_model=schemas.course)
def delete_course(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an course.
    """
    course = crud.course.get(db=db, id=id)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    if not crud.user.is_superuser(current_user) and (course.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    course = crud.course.remove(db=db, id=id)
    return course
