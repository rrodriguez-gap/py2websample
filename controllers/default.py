def article():
    grid = SQLFORM.grid(db.articles, user_signature=False)
    return dict(grid=grid)
 
def store():
    grid = SQLFORM.grid(db.stores, user_signature=False)
    return dict(grid=grid)

def index():
	return dict(message=T('Super Zapato'))