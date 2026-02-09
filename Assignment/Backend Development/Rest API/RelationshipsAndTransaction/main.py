@app.post("/users/{user_id}/items/")
def create_item_for_user(
    user_id: int,
    item: ItemCreate,
    db: Session = Depends(get_db)
):
    try:
        db_item = ItemDB(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()          # Transaction commit
        db.refresh(db_item)
        return db_item

    except Exception as e:
        db.rollback()        # Rollback on error
        raise HTTPException(status_code=400, detail=str(e))
