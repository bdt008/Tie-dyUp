from app.models import db, Store, environment, SCHEMA


demo_store = Store (
    name = "Demo Store", about = "This is the demo store to show you all the goodies", cover_image_url = "", user_id = "1"
)
gucci = Store (
    name = "gucci", about = "Quality Is remembered long after price is forgotten.", cover_image_url = "", user_id = "2"
)
dior = Store (
    name = "dior", about = "to leave a legacy of beauty and be fully committed", cover_image_url = "", user_id = "2"
)
chanel = Store (
    name = "chanel", about = "It's All About Seconds.", cover_image_url = "", user_id = "3"
)
hermes = Store (
    name = "hermes", about = "You dream it up Hermes makes it happen", cover_image_url = "", user_id = "4"
)
prada = Store (
    name = "prada", about = "Be seen, be heard.", cover_image_url = "", user_id = "5"
)
balenciaga = Store (
    name = "balenciaga", about = "Live to Love", cover_image_url = "", user_id = "6"
)
cartier = Store (
    name = "cartier", about = "Never imitate, always innovate", cover_image_url = "", user_id = "7"
)




def seed_servers():
    db.session.add(demo_store)
    db.session.add(gucci)
    db.session.add(dior)
    db.session.add(chanel)
    db.session.add(hermes)
    db.session.add(prada)
    db.session.add(balenciaga)
    db.session.add(cartier)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the servers table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_servers():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.servers RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM servers")

    db.session.commit()
