from faker import Faker
from models import User, Games, Bets, SessionLocal
import random
from datetime import datetime

fake = Faker()

def clear_tables():
    """Deletes all data from tables before seeding."""
    db = SessionLocal()
    try:
        db.query(Bets).delete()
        db.query(Games).delete()
        db.query(User).delete()
        db.commit()
        print("All tables cleared.")
    except Exception as e:
        db.rollback()
        print(f"An error occurred while clearing tables: {e}")
    finally:
        db.close()

def seed_users(n):
    """Seeds the User table with n users."""
    db = SessionLocal()
    try:
        for _ in range(n):
            user = User(
                name=fake.name(),
                email=fake.email(),
                password=fake.password(),
                balance=round(random.uniform(100.0, 1000.0), 2)
            )
            db.add(user)
        db.commit()
        print(f"{n} users seeded.")
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

def seed_games(n):
    """Seeds the Games table with n games."""
    db = SessionLocal()
    try:
        for _ in range(n):
            game = Games(
                name=fake.word(),
                date_time=datetime.strptime("2025-03-02 23:58:51", "%Y-%m-%d %H:%M:%S"),
                status=random.choice(['scheduled', 'ongoing', 'completed']),
                odds=round(random.uniform(1.0, 5.0), 2)
            )
            db.add(game)
        db.commit()
        print(f"{n} games seeded.")
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

def seed_bets(n):
    """Seeds the Bets table with n bets, ensuring users and games exist."""
    db = SessionLocal()
    try:
        user_ids = [user.id for user in db.query(User).all()]
        game_ids = [game.id for game in db.query(Games).all()]

        if not user_ids or not game_ids:
            print("Skipping bet seeding: No users or games available.")
            return

        for _ in range(n):
            bet = Bets(
                user_id=random.choice(user_ids),
                game_id=random.choice(game_ids),
                amount=round(random.uniform(10.0, 500.0), 2),
                bet_type=random.choice(['win', 'lose', 'draw']),
                pay_out=round(random.uniform(20.0, 1000.0), 2)
            )
            db.add(bet)
        db.commit()
        print(f"{n} bets seeded.")
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == '__main__':
    clear_tables()
    seed_users(10)
    seed_games(5)
    seed_bets(20)
    print("Database seeded successfully!")
