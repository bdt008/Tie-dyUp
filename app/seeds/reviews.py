from app.models import db, Review, environment, SCHEMA

#demoUser reviews
review1 = Review (
    user_id = 1, content = "My co-worker Fate has one of these. He says it looks tall.", star_rating = 4, product_id = 1, store_id = 1
)
review2 = Review (
    user_id = 1, content = "I saw one of these in Algeria and I bought one.", star_rating = 5, product_id = 7, store_id = 2
)
review3 = Review (
    user_id = 1, content = "The box this comes in is 3 meter by 5 foot and weights 11 kilogram.", star_rating = 3, product_id = 11, store_id = 3
)
review4 = Review (
    user_id = 1, content = "i use it profusely when i'm in my garage.", star_rating = 2, product_id = 16, store_id = 4
)

#rylan reviews
review5 = Review (
    user_id = 2, content = "This cloths works so well. It delightedly improves my football by a lot.", star_rating = 3, product_id = 1, store_id = 1
)
review6 = Review (
    user_id = 2, content = "one of my hobbies is poetry. and when i'm writing poems this works great.", star_rating = 4, product_id = 16, store_id = 2
)
review7 = Review (
    user_id = 2, content = "talk about lust!!", star_rating = 2, product_id = 19, store_id = 3
)
review8 = Review (
    user_id = 2, content = "talk about sadness!!", star_rating = 1, product_id = 24, store_id = 4
)
review9 = Review (
    user_id = 2, content = "My neighbor Karly has one of these. She works as a gambler and she says it looks tall.", star_rating = 5, product_id = 29, store_id = 5
)

#emilee reviews
review10 = Review (
    user_id = 3, content = "My neighbor Allean has one of these. She works as a sky diver and she says it looks weedy.", star_rating = 5, product_id = 1, store_id = 1
)
review11 = Review (
    user_id = 3, content = "heard about this on compas radio, decided to give it a try.", star_rating = 3, product_id = 6, store_id = 4
)
review12 = Review (
    user_id = 3, content = "I absolutely love this shirt! The fabric is so soft and comfortable, I never want to take it off.", star_rating = 4, product_id = 11, store_id = 5
)

#meredith reviews
review13 = Review (
    user_id = 4, content = "I was worried about the sizing, but it fits perfectly and is so comfortable to wear.", star_rating = 4, product_id = 2, store_id = 1
)
review14 = Review (
    user_id = 4, content = "I love the attention to detail in this shirt. It's well made and I know it will last a long time.", star_rating = 3, product_id = 16, store_id = 2
)
review15 = Review (
    user_id = 4, content = "I was worried about the sizing, but it fits perfectly and is so comfortable to wear.", star_rating = 3, product_id = 19, store_id = 3
)
review16 = Review (
    user_id = 4, content = "The fabric is so soft, it feels like I'm wearing a cloud!", star_rating = 4, product_id = 24, store_id = 4
)

#elwood reviews
review17 = Review (
    user_id = 5, content = "I love the vibrant colors, they brighten up my day!", star_rating = 5, product_id = 1, store_id = 1
)
review18 = Review (
    user_id = 5, content = "I was skeptical about the quality, but it exceeded my expectations.", star_rating = 5, product_id = 29, store_id = 6
)
review19 = Review (
    user_id = 5, content = "The detailing on this shirt is impeccable, it's a work of art.", star_rating = 5, product_id = 32, store_id = 7
)

#lark reviews
review20 = Review (
    user_id = 6, content = "The breathable fabric keeps me cool on hot summer days.", star_rating = 4, product_id = 1, store_id = 1
)
review21 = Review (
    user_id = 6, content = "The durability of this shirt is impressive, it can withstand rough wear.", star_rating = 3, product_id = "", store_id = 6
)
review22 = Review (
    user_id = 6, content = "The sizing is accurate, it fits me perfectly.", star_rating = 2, product_id = 2, store_id = 7
)
review23= Review (
    user_id = 6, content = "The neckline is so flattering, it accentuates my face.", star_rating = 1, product_id = "", store_id = 8
)
review24 = Review (
    user_id = 6, content = "I love the subtle design, it adds a touch of sophistication to my look.", star_rating = 5, product_id = "", store_id = 2
)

#marnie reviews
review25 = Review (
    user_id = 7, content = "I love the versatility of this shirt, I can wear it to work or for a night out.", star_rating = 5, product_id = 1, store_id = 1
)
review26 = Review (
    user_id = 7, content = "The cuffs are the perfect fit, they don't fall down.", star_rating = 4, product_id = "", store_id = 2
)
review27 = Review (
    user_id = 7, content = "I love the timeless design of this shirt, it's a classic piece.", star_rating = 5, product_id = "", store_id = 3
)

#bobbie reviews
review28 = Review (
    user_id = 8, content = "The material is so durable, it can withstand daily wear and tear.", star_rating = 3, product_id = 1, store_id = 1
)
review29 = Review (
    user_id = 8, content = "I love the feel of this shirt, it's like a second skin.", star_rating = 3, product_id = "", store_id = 8
)



def seed_servers():
    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.add(review7)
    db.session.add(review8)
    db.session.add(review9)
    db.session.add(review10)
    db.session.add(review11)
    db.session.add(review12)
    db.session.add(review13)
    db.session.add(review14)
    db.session.add(review15)
    db.session.add(review16)
    db.session.add(review17)
    db.session.add(review18)
    db.session.add(review19)
    db.session.add(review20)
    db.session.add(review21)
    db.session.add(review22)
    db.session.add(review23)
    db.session.add(review24)
    db.session.add(review25)
    db.session.add(review26)
    db.session.add(review27)
    db.session.add(review28)
    db.session.add(review29)

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
