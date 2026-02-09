from typing import Optional

@app.get("/items/")
def read_items(
    skip: int = 0,
    limit: int = 100,
    q: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(ItemDB)

    if q:
        # Full-text search or ILIKE
        query = query.filter(ItemDB.title.ilike(f"%{q}%"))

    items = query.offset(skip).limit(limit).all()
    return items
