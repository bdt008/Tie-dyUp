from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', image_profile_url = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGVvcGxlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60", password='password', street_number = "713", street_name = "North Street", city = "Philadelphia", state = "Pennsylvania", zip_code = "19123", telephone = "4129973936")
    rylan = User(
        username='Rylan', email='Rylan@aa.io', image_profile_url = "https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8cGVvcGxlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60", password='password', street_number = "6100", street_name = "Algon Ave", city = "Philadelphia", state = "Pennsylvania", zip_code = "19111", telephone = "2152254953")
    emilee = User(
        username='emilee', email='emilee@aa.io', image_profile_url = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fHBlb3BsZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", password='password', street_number = "2100", street_name = "Fraley Street", city = "Philadelphia", state = "Pennsylvania", zip_code = "19124", telephone = "4125594477")
    meredith = User(
        username='meredith', email='meredith@aa.io', image_profile_url = "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjZ8fHBlb3BsZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", password='password', street_number = "8223", street_name = "Roosevelt Boulevard", city = "Philadelphia", state = "Pennsylvania", zip_code = "19152", telephone = "7249499204")
    elwood = User(
        username='elwood', email='elwood@aa.io', image_profile_url = "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8cGVvcGxlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60", password='password', street_number = "4318", street_name = "Princeton Avenue", city = "Philadelphia", state = "Pennsylvania", zip_code = "19135", telephone = "8142961088")
    lark = User(
        username='lark', email='lark@aa.io', image_profile_url = "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTZ8fHBlb3BsZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", password='password', street_number = "1900", street_name = "Wharton Street", city = "Philadelphia", state = "Pennsylvania", zip_code = "19146", telephone = "4842502357")
    marnie = User(
        username='marnie', email='marnie@aa.io', image_profile_url = "https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDh8fHBlb3BsZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", password='password', street_number = "4000", street_name = "Irving Street", city = "Philadelphia", state = "Pennsylvania", zip_code = "19104", telephone = "4842502357")
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', image_profile_url = "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjN8fHBlb3BsZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60", password='password', street_number = "4373", street_name = "Main Street", city = "Philadelphia", state = "Pennsylvania", zip_code = "19127", telephone = "4842502357")

    db.session.add(demo)
    db.session.add(rylan)
    db.session.add(emilee)
    db.session.add(meredith)
    db.session.add(elwood)
    db.session.add(lark)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
