import json
from app.database import Base, engine, SessionLocal
from app.models import Product


def create_tables():
    Base.metadata.create_all(bind=engine)


def seed_products():
    db = SessionLocal()
    try:
        existing_count = db.query(Product).count()
        if existing_count > 0:
            print(f"Products already seeded ({existing_count} records). Skipping.")
            return

        sample_products = [
            {
                "name": "Clear Pore Gel Cleanser",
                "brand": "DermBasics",
                "ingredient_tags": ["salicylic_acid", "niacinamide"],
                "skin_types": ["oily", "combination"],
                "conditions_targeted": ["acne"],
                "priority": 92,
                "price": 12.99,
                "affiliate_url": "https://example.com/affiliate/clear-pore-gel-cleanser",
                "image_url": "https://example.com/images/clear-pore-gel-cleanser.jpg",
            },
            {
                "name": "Oil Balance Serum",
                "brand": "SkinFlow",
                "ingredient_tags": ["niacinamide"],
                "skin_types": ["oily", "combination", "sensitive"],
                "conditions_targeted": ["acne", "pigmentation"],
                "priority": 88,
                "price": 15.50,
                "affiliate_url": "https://example.com/affiliate/oil-balance-serum",
                "image_url": "https://example.com/images/oil-balance-serum.jpg",
            },
            {
                "name": "Bright C Complex",
                "brand": "GlowLabs",
                "ingredient_tags": ["vitamin_c", "alpha_arbutin"],
                "skin_types": ["dry", "combination", "sensitive"],
                "conditions_targeted": ["pigmentation"],
                "priority": 95,
                "price": 22.00,
                "affiliate_url": "https://example.com/affiliate/bright-c-complex",
                "image_url": "https://example.com/images/bright-c-complex.jpg",
            },
            {
                "name": "Spot Correct Night Essence",
                "brand": "ToneFix",
                "ingredient_tags": ["alpha_arbutin", "niacinamide"],
                "skin_types": ["dry", "combination", "oily"],
                "conditions_targeted": ["pigmentation"],
                "priority": 84,
                "price": 18.75,
                "affiliate_url": "https://example.com/affiliate/spot-correct-night-essence",
                "image_url": "https://example.com/images/spot-correct-night-essence.jpg",
            },
            {
                "name": "Hydra Barrier Cream",
                "brand": "MoistuRelief",
                "ingredient_tags": ["hyaluronic_acid", "ceramides"],
                "skin_types": ["dry", "sensitive"],
                "conditions_targeted": ["dry_skin"],
                "priority": 97,
                "price": 19.99,
                "affiliate_url": "https://example.com/affiliate/hydra-barrier-cream",
                "image_url": "https://example.com/images/hydra-barrier-cream.jpg",
            },
            {
                "name": "Deep Hydration Gel",
                "brand": "AquaSkin",
                "ingredient_tags": ["hyaluronic_acid", "glycerin"],
                "skin_types": ["dry", "combination", "sensitive"],
                "conditions_targeted": ["dry_skin"],
                "priority": 90,
                "price": 14.40,
                "affiliate_url": "https://example.com/affiliate/deep-hydration-gel",
                "image_url": "https://example.com/images/deep-hydration-gel.jpg",
            },
            {
                "name": "Calm Skin Lotion",
                "brand": "DermaCalm",
                "ingredient_tags": ["ceramides", "niacinamide"],
                "skin_types": ["sensitive", "dry"],
                "conditions_targeted": ["dry_skin", "healthy"],
                "priority": 82,
                "price": 16.20,
                "affiliate_url": "https://example.com/affiliate/calm-skin-lotion",
                "image_url": "https://example.com/images/calm-skin-lotion.jpg",
            },
            {
                "name": "Daily Defense Moisturizer",
                "brand": "PureLayer",
                "ingredient_tags": ["glycerin", "niacinamide"],
                "skin_types": ["oily", "combination", "dry"],
                "conditions_targeted": ["healthy"],
                "priority": 78,
                "price": 13.30,
                "affiliate_url": "https://example.com/affiliate/daily-defense-moisturizer",
                "image_url": "https://example.com/images/daily-defense-moisturizer.jpg",
            },
            {
                "name": "Gentle Renewal Cleanser",
                "brand": "FreshMend",
                "ingredient_tags": ["ceramides", "hyaluronic_acid"],
                "skin_types": ["sensitive", "dry", "combination"],
                "conditions_targeted": ["healthy", "dry_skin"],
                "priority": 76,
                "price": 11.80,
                "affiliate_url": "https://example.com/affiliate/gentle-renewal-cleanser",
                "image_url": "https://example.com/images/gentle-renewal-cleanser.jpg",
            },
        ]

        for item in sample_products:
            product = Product(
                name=item["name"],
                brand=item["brand"],
                ingredient_tags=json.dumps(item["ingredient_tags"]),
                skin_types=json.dumps(item["skin_types"]),
                conditions_targeted=json.dumps(item["conditions_targeted"]),
                priority=item["priority"],
                price=item["price"],
                affiliate_url=item["affiliate_url"],
                image_url=item["image_url"],
            )
            db.add(product)

        db.commit()
        print(f"Seeded {len(sample_products)} products.")
    finally:
        db.close()


if __name__ == "__main__":
    create_tables()
    seed_products()
    print("Database setup complete.")
