from app.models import db, Product, environment, SCHEMA

#store 1 Demo-Store
item1 = Product(
    name = "Hank Slim Fit Dress Shirt", description = "Crisp and clean, this wardrobe-staple dress shirt made of breathable cotton with stretch irons easily to bring a smart finish to any formal look.", price = 25.60, image_url = "https://n.nordstrommedia.com/id/sr3/87cca9fa-7504-42b7-b65a-79c6bdf663ba.jpeg?crop=pad&pad_color=FFF&format=jpeg&w=780&h=1196", brand = "BOSS", catagory = "shirt", store_id = "1"
)
item2 = Product(
    name = "Men's Delaware Straight Leg Jeans", description = "Crafted from wrinkle-resistant stretch denim, these straight-leg jeans are perfect for casual workdays.", price = 31.60 , image_url = "https://n.nordstrommedia.com/id/sr3/e23bce01-5337-47ea-92df-3ae7d2e2dfb3.jpeg?crop=pad&pad_color=FFF&format=jpeg&w=780&h=1196", brand = "BOSS", catagory = "pants", store_id = "1"
)
item3 = Product(
    name = "Brace Tonic Crewneck T-Shirt", description = "Supremely soft cotton construction defines a classic T-shirt stamped with a bit of cool branding.", price = "11.00", image_url = "https://n.nordstrommedia.com/id/sr3/567a004c-a513-4115-b24c-7ec7ffd9e515.jpeg?crop=pad&pad_color=FFF&format=jpeg&w=780&h=1196", brand = "ALLSAINTS", catagory = "shirt", store_id = "1"
)
item4 = Product(
    name = "Stretch Cotton Body-Con Minidress", description = "Fashioned with center-seam details at the front and back, this figure-flaunting mini is cut from stretch-enhanced cotton softened by an enzyme wash.", price = 94.00, image_url = "https://n.nordstrommedia.com/id/sr3/5ae479c1-ed2b-4379-b1a3-b005d5f99666.jpeg?crop=pad&pad_color=FFF&format=jpeg&w=780&h=1196", brand = "ALEXANDER WANG", catagory = "dress", store_id = "1"
)
item5 = Product(
    name = "High Waist Trousers", description = "Cultivate an elevated aesthetic in high-waist trousers designed in a sleek, slim fit.", price = 198.00, image_url = "https://n.nordstrommedia.com/id/sr3/2e144359-c969-4789-ac93-8f217613e4d5.jpeg?crop=pad&pad_color=FFF&format=jpeg&w=780&h=1196", brand = "CAROLINA HERRERA", catagory = "pants", store_id = "1"
)

#store 2 Gucci
item6 = Product(
    name = "Ophidia jumbo GG small shoulder bag", description = "The jumbo GG explores a new, maximalist version of the historic monogram, animating this small shoulder bag in camel and mint.", price = 358.00, image_url = "https://media.gucci.com/style/HEXF1E9FB_Center_0_0_800x800/1674083739/499621_UKMBG_9549_001_065_0000_Light-Ophidia-jumbo-GG-small-shoulder-bag.jpg", brand = "GUCCI", catagory = "handbag", store_id = "2"
)
item7 = Product(
    name = "Striped jacquard wool cotton dress", description = "This wool and cotton jacquard dress elevates the classic knit dress with the House's tongue-in-cheek design detail and color combination.", price = 525.00 , image_url = "https://media.gucci.com/style/HEXF1E9FB_Center_0_0_800x800/1675357262/727173_XKCZH_6367_001_100_0000_Light-Striped-jacquard-wool-cotton-dress.jpg", brand = "GUCCI", catagory = "dress", store_id = "2"
)
item8 = Product(
    name = "GG jacquard wool knit sweater", description = "A mix of colors and textures overlap to form new, unconventional designs", price = 170.00 , image_url = "https://media.gucci.com/style/HEXF1E9FB_Center_0_0_800x800/1669919497/729380_XKC0J_7021_001_100_0000_Light-GG-jacquard-wool-knit-sweater.jpg", brand = "GUCCI", catagory = "shirt", store_id = "2"
)
item9 = Product(
    name = "Textured gabardine cropped pant", description = "These taupe textured wide-leg pants speak to the end of seasonality when it comes to fashion.", price = 160.00, image_url = "https://media.gucci.com/style/HEXF1E9FB_Center_0_0_800x800/1674757804/723677_ZAHE0_2144_001_100_0000_Light-Textured-gabardine-cropped-pant.jpg", brand = "GUCCI", catagory = "pants", store_id = "2"
)
item10 = Product(
    name = "GG rombus print neoprene sweatshirt", description = "The various materials are presented as a patchwork design, resulting in an eclectic mix of textures and colors.", price = 198.00, image_url = "https://media.gucci.com/style/HEXF1E9FB_Center_0_0_800x800/1671475541/727895_XJE8M_2454_001_100_0000_Light-GG-rombus-print-neoprene-sweatshirt.jpg", brand = "GUCCI", catagory = "shirt", store_id = "2"
)

#store 3 dior
item11 = Product(
    name = "WALK'N'DIOR SNEAKER", description = "he Walk'n'Dior sneaker presents a nude embroidered cotton Dior Oblique motif.", price = 105.00 , image_url = "https://media.dior.com/couture/ecommerce/media/catalog/product/L/v/1633689912_KCK211OBE_S21U_E02_GHC.jpg?imwidth=800", brand = "DIOR", catagory = "shoes", store_id = "3"
)
item12 = Product(
    name = "30 MONTAIGNE BAR JACKET", description = "The Bar Jacket is an emblematic style from the New Look collection, first created by Christian Dior in 1947.", price = 470.00, image_url = "https://media.dior.com/couture/ecommerce/media/catalog/product/3/w/1586461503_841V01A1166_X0200_E01_GHC.jpg?imwidth=800", brand = "DIOR", catagory = "shirt", store_id = "3"
)
item13 = Product(
    name = "CHRISTIAN DIOR' SHORT-SLEEVED SWEATER", description = "The sweater combines modernity and elegance. Delicately crafted in ecru cashmere and wool knit", price = 230.00, image_url = "https://media.dior.com/couture/ecommerce/media/catalog/product/0/8/1626091097_154S09AM305_X5801_E01_GHC.jpg?imwidth=800", brand = "DIOR", catagory = "shirt", store_id = "3"
)
item14 = Product(
    name = "DIOR CHEZ MOI SHORTS", description = "The shorts highlight the hallmark blue Dior Oblique motif. Crafted in silk twill,", price = 250.00 , image_url = "https://media.dior.com/couture/ecommerce/media/catalog/product/2/S/1612446374_121P20A6608_X5803_E01_GHC.jpg?imwidth=800", brand = "DIOR", catagory = "pants", store_id = "3"
)
item15 = Product(
    name = "D-RACER ANKLE BOOT", description = "The D-Racer ankle boot is distinguished by a timeless look with a modern Dior twist.", price = 149.00, image_url = "https://media.dior.com/couture/ecommerce/media/catalog/product/P/M/1660813634_KCI780VEA_S03W_E02_GHC.jpg?imwidth=800", brand = "DIOR", catagory = "shoes", store_id = "3"
)

#store 4 chanel
item16 = Product(
    name = "CHANEL Pullover", description = "Mixed Fibers & Cashmere Embroidered", price = 485.00, image_url = "https://buyma-global-prod-img-temp.s3.amazonaws.com/direct_upload%2Fproducts%2Fadb3f594-dcbc-47a8-a54a-b418d7dea7fc%2Fc7e356be-5678-421f-927b-89fed5344753.jpg", brand = "CHANEL", catagory = "shirt", store_id = "4"
)
item17 = Product(
    name = "CHANEL Shorts", description = "Denim & Cotton Shorts from CHANEL, Short, Elegant Style, Casual Style, Plain", price = 329.00, image_url = "https://cdn-images.buyma.com/imgdata/item/220309/0080532625/437024688/428.jpg", brand = "CHANEL", catagory = "pants", store_id = "4"
)
item18 = Product(
    name = "CHANEL Dress", description = "Dresses from CHANEL, Elegant Style, Casual Style, Sleeveless, Long", price = 154.00, image_url = "https://cdn-images.buyma.com/imgdata/item/220506/0082551332/452851413/428.jpg", brand = "CHANEL", catagory = "dress", store_id = "4"
)

#store 5 hermes
item19 = Product(
    name = "Zipped mock neck sweater", description = "Long-sleeve sweater with mock neck collar in braided cotton voile", price = 240.00 , image_url = "https://assets.hermes.com/is/image/hermesproduct/zipped-mock-neck-sweater--352000HA1V-worn-1-0-0-800-800_b.jpg", brand = "HERMES", catagory = "shirt", store_id = "5"
)
item20 = Product(
    name = "Saint Germain fitted pants", description = "Fitted pants in stretch cotton twill", price = 150.00, image_url = "https://assets.hermes.com/is/image/hermesproduct/saint-germain-fitted-pants--355020H301-worn-1-0-0-800-800_b.jpg", brand = "HERMES", catagory = "pants", store_id = "5"
)
item21 = Product(
    name = "Maillon Chaine d'Ancre crewneck sweater", description = "Long-sleeve crewneck sweater in cashmere with Maillon Chaine d'Ancre detail", price = 225.00, image_url = "https://assets.hermes.com/is/image/hermesproduct/maillon-chaine-d-ancre-crewneck-sweater--357020HA94-worn-1-0-0-800-800_b.jpg", brand = "HERMES", catagory = "shirt", store_id = "5"
)
item22 = Product(
    name = "HERMES Beach Shirt", description = "Beach shirt in plain cotton poplin", price = 115.00 , image_url = "https://assets.hermes.com/is/image/hermesproduct/beach-shirt--3E3612D801-worn-1-0-0-800-800_b.jpg", brand = "HERMES", catagory = "shirt", store_id = "5"
)
item23 = Product(
    name = "HERMES Straight Leg Pants", description = "Straight leg pants in Milano jersey", price = 175.00 , image_url = "https://assets.hermes.com/is/image/hermesproduct/straight-leg-pants--3E0421DJ02-worn-1-0-0-800-800_b.jpg", brand = "HERMES", catagory = "pants", store_id = "5"
)

#store 6 prada
item24 = Product(
    name = "Jersey T-shirt", description = "Pure lines reveal complex simplicity in this jersey tee with minimalist allure.", price = 107.00 , image_url = "https://www.prada.com/content/dam/pradabkg_products/3/346/34642/10UPF0009/34642_10UP_F0009_S_231_SLF.jpg/jcr:content/renditions/cq5dam.web.hebebed.800.800.jpg", brand = "PRADA", catagory = "shirt", store_id = "6"
)
item25 = Product(
    name = "Prada America's Cup Soft rubber and bike fabric sneakers", description = "The America's Cup sneaker, which is part of the Prada identity, is reinvented with new materials and colors that instill it with a new contemporary spirit.", price = 75.00, image_url = "https://www.prada.com/content/dam/pradabkg_products/3/3E6/3E6500/3LLJF0002/3E6500_3LLJ_F0002_F_025_SLR.jpg/jcr:content/renditions/cq5dam.web.hebebed.800.800.jpg", brand = "PRADA", catagory = "shoes", store_id = "6"
)
item26 = Product(
    name = "Kid mohair pants", description = "These kid mohair pants with a masculine cut and sartorial silhouette reflect the inherent complex simplicity of Prada collections.", price = 205.00, image_url = "https://www.prada.com/content/dam/pradabkg_products/P/P28/P282G/12I1F0304/P282G_12I1_F0304_S_231_SLF.jpg/jcr:content/renditions/cq5dam.web.hebebed.800.800.jpg", brand = "PRADA", catagory = "pants", store_id = "6"
)
item27 = Product(
    name = "Re-Nylon shorts", description = "Sporty inspiration and technological innovation meet in these shorts that take the classic style", price = 129.00, image_url = "https://www.prada.com/content/dam/pradabkg_products/2/22S/22S757/11FCF0002/22S757_11FC_F0002_S_192_SLF.jpg/jcr:content/renditions/cq5dam.web.hebebed.800.800.jpg", brand = "PRADA", catagory = "pants", store_id = "6"
)
item28 = Product(
    name = "Long-sleeved sweatshirt", description = "This oversized sweatshirt with ribbed knit trim has sporty charm and sleek allure.", price = 142.00 , image_url = "https://www.prada.com/content/dam/pradabkg_products/1/134/134668/11LNF0031/134668_11LN_F0031_S_231_SLF.jpg/jcr:content/renditions/cq5dam.web.hebebed.800.800.jpg", brand = "PRADA", catagory = "shirt", store_id = "6"
)

#store 7 balenciaga
item29 = Product(
    name = "WOMEN'S MINI DRESS IN BLACK", description = "Garde-Robe is made up of wardrobe staples in elevated cuts, sharp finishing, and luxe materials", price = 195.00 , image_url = "https://balenciaga.dam.kering.com/m/27579f582afd2d2d/Large-725079TMO701000_G.jpg?v=4", brand = "BALENCIAGA", catagory = "dress", store_id = "7"
)
item30 = Product(
    name = "WOMEN'S LOOSE SHORTS IN BLACK", description = "Loose Shorts in black stretch virgin wool are from the look 31 of the Balenciaga's Spring 23", price = 115.00 , image_url = "https://balenciaga.dam.kering.com/m/289564253430cca1/Large-725514TNT111000_G.jpg?v=5", brand = "BALENCIAGA", catagory = "pants", store_id = "7"
)
item31 = Product(
    name = "MEN'S BALENCIAGA ADIDAS TRIPLE S SNEAKER IN WHITE", description = "Adidas Triple S Sneaker in white, black and grey double foam and mesh", price = 125.00, image_url = "https://balenciaga.dam.kering.com/m/56412943d86bd1a5/Large-710021W2ZB19112_F.jpg?v=4", brand = "BALENCIAGA", catagory = "shoes", store_id = "7"
)

#store 8 cartier
item32 = Product(
    name = "JUSTE UN CLOU BRACELET", description = "Juste un Clou bracelet, small model, 18K yellow gold", price = 340.00, image_url = "https://www.cartier.com/dw/image/v2/BGTJ_PRD/on/demandware.static/-/Sites-cartier-master/default/dwbf8c00c9/images/large/637708806668716578-2059323.png?sw=750&sh=750&sm=fit&sfrm=png", brand = "CARTIER", catagory = "jewelry", store_id = "8"
)
item33 = Product(
    name = "TRINITY RING CLASSIC", description = "Trinity ring, medium model, 18K white gold", price = 149.00 , image_url = "https://www.cartier.com/dw/image/v2/BGTJ_PRD/on/demandware.static/-/Sites-cartier-master/default/dw7a64195b/images/large/637708725821502325-2059310.png?sw=750&sh=750&sm=fit&sfrm=png", brand = "CARTIER", catagory = "jewelry", store_id = "8"
)
item34 = Product(
    name = "Clash de Cartier bracelet", description = "Clash de Cartier bracelet, medium model, rhodiumized 18K white gold", price = 990.00 , image_url = "https://www.cartier.com/dw/image/v2/BGTJ_PRD/on/demandware.static/-/Sites-cartier-master/default/dwd49d3233/images/large/637708809736526526-2196273.png?sw=750&sh=750&sm=fit&sfrm=png", brand = "CARTIER", catagory = "jewelry", store_id = "8"
)
item35 = Product(
    name = "LOVE RING 3 DIAMONDS", description = "LOVE ring, 18K rose gold (750/1000), set with 3 brilliant-cut diamonds totaling 0.22 carats", price = 385.00, image_url = "https://www.cartier.com/dw/image/v2/BGTJ_PRD/on/demandware.static/-/Sites-cartier-master/default/dwd0210907/images/large/637708746037369393-2116892.png?sw=750&sh=750&sm=fit&sfrm=png", brand = "CARTIER", catagory = "jewelry", store_id = "8"
)
item36 = Product(
    name = "LOVE NECKLACE, DIAMOND-PAVED", description = "LOVE necklace, 18K yellow gold (750/1000), set with 54 brilliant-cut diamonds totaling 0.34", price = 845.00, image_url = "https://www.cartier.com/dw/image/v2/BGTJ_PRD/on/demandware.static/-/Sites-cartier-master/default/dwc842a2e5/images/large/637708815445251209-2116941.png?sw=750&sh=750&sm=fit&sfrm=png", brand = "CARTIER", catagory = "jewelry", store_id = "8"
)

def seed_servers():
    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.add(item5)
    db.session.add(item6)
    db.session.add(item7)
    db.session.add(item8)
    db.session.add(item9)
    db.session.add(item10)
    db.session.add(item11)
    db.session.add(item12)
    db.session.add(item13)
    db.session.add(item14)
    db.session.add(item15)
    db.session.add(item16)
    db.session.add(item17)
    db.session.add(item18)
    db.session.add(item19)
    db.session.add(item20)
    db.session.add(item21)
    db.session.add(item22)
    db.session.add(item23)
    db.session.add(item24)
    db.session.add(item25)
    db.session.add(item26)
    db.session.add(item27)
    db.session.add(item28)
    db.session.add(item29)
    db.session.add(item30)
    db.session.add(item31)
    db.session.add(item32)
    db.session.add(item33)
    db.session.add(item34)
    db.session.add(item35)
    db.session.add(item36)
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
