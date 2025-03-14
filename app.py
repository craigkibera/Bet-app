from models import Games, User, Bets, SessionLocal
from passlib.hash import bcrypt
from tabulate import tabulate
import datetime
import ipdb
# ipdb.set_trace()
def view_all_games():
    db = SessionLocal()
    try:
        games = db.query(Games).all()
        
        if not games:
            print("No game found")
            return

        headers = ["ID", "Name", "Date", "Status", "Odds", "Created At"]
        rows = [
            [
                game.id,
                game.name,
                game.date_time,
                game.status,
                game.odds,
                game.created_at.strftime("%Y-%m-%d %H:%M:%S") if game.created_at else "N/A"
            ]
            for game in games
        ]
        print(tabulate(rows, headers, tablefmt="pretty"))

    except Exception as e:
        print("An error occurred:", e)

    finally:
        db.close()


def add_game():
    name = input("Game Name: ")
    date = input("Game Date: ")
    odds = input("Game Odds: ")

   
    db = SessionLocal()
    try:
        new_game = Games(name=name, date_time=date, odds=float(odds))
        print(new_game)
        db.add(new_game)
        db.commit()
        db.refresh(new_game)
        print(f"Game added successfully with ID: {new_game.id}")
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

def place_bets():
    amount = input("Bet amount: ")
    pay_out = input("Bet pay_out: ")
    bet_type = input("Bet bet_type : ")



    db = SessionLocal()
    try:
        new_bet = Bets(user_id=1, game_id=1, amount=float(amount), pay_out=float(pay_out), bet_type=bet_type)
        print(new_bet)
        # new_bet = Bets(amount=float(50), pay_out=float(50), bet_type="rand_string", user_id=1, game_id=1)
        db.add(new_bet)
        db.commit()
        db.refresh(new_bet)
        print(f"Bet added successfully with ID: {new_bet.id}")
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

def view_all_bets():
    db = SessionLocal()
    try:
        bets = db.query(Bets).all()
        
        if not bets:
            print("No bet found")
            return

        headers = ["ID", "Amount", "Pay Out", "Bet Type", "Created At"]
        rows = [
            [
                bet.id,
                bet.amount,
                bet.pay_out,
                bet.bet_type,
                bet.created_at.strftime("%Y-%m-%d %H:%M:%S") if bet.created_at else "N/A"
            ]
            for bet in bets
        ]
        print(tabulate(rows, headers, tablefmt="pretty"))

    except Exception as e:
        print("An error occurred:", e)

    finally:
        db.close()

def sign_up():
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    password_confirrm = input("Confirm Password: ")

    if password != password_confirrm:
        print("Passwords do not match")
        return

    db = SessionLocal()
    try:
        hashed_password = bcrypt.hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print(f"User added successfully with as {new_user.name}")
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

def login():
    email = input("Email: ")
    password = input("Password: ")

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user or not bcrypt.verify(password, user.password):
            print("Invalid email or password")
            return

        print(f"Welcome back, {user.name}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        db.close()

def remove_bet():
    db = SessionLocal()
    try:
        bets = db.query(Bets).all()
        
        if not bets:
            print("No bet found")
            return

        headers = ["ID", "Amount", "Pay Out", "Bet Type", "Created At"]
        rows = [
            [
                bet.id,
                bet.amount,
                bet.pay_out,
                bet.bet_type,
                bet.created_at.strftime("%Y-%m-%d %H:%M:%S") if bet.created_at else "N/A"
            ]
            for bet in bets
        ]
        print(tabulate(rows, headers, tablefmt="pretty"))

        bet_id = input("Enter the ID of the bet to remove: ")
        bet = db.query(Bets).filter(Bets.id == bet_id).first()
        if not bet:
            print("Bet not found")
            return

        db.delete(bet)
        db.commit()
        print(f"Bet with ID {bet_id} removed successfully")
    except Exception as e:
        db.rollback()
        print("An error occurred:", e)
    finally:
        db.close()


def menu():
    while True:
        print("\nBetting CLI")
        print("\nSelect an option to continue")
        print("1. Sign Up")
        print("2. Login")
        print("3. View all Games")
        print("4. Add Game")
        print("5. Place Bet")
        print("6. View all Bets")
        print("7. Remove bet")
        print("8. Exit")
        

        
        choice = input("Enter your choice: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            login()
        elif choice == '3':
            view_all_games()
        elif choice == '4':
            add_game()
        elif choice == '5':
            place_bets()
        elif choice == '6':
            view_all_bets()
        elif choice == '7':
            remove_bet()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    menu()