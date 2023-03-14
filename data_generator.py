import random 
import string 
from datetime import datetime, timedelta

user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))

def generate_transaction() -> dict:
    random_user_id = random.choice(user_ids)
    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()
    # User can't send message to himself
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)
    # Generate a random amount
    amount = random.randint(100, 2000)
    # Generate a random datetime between 9am and 5pm on a random day in January 2023
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 31)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    # Format the datetime as a string
    datetime_str = random_date.strftime('%d %H:%M')

    info = {
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'amount': amount,
        'datetime': datetime_str
    }

    return info

    

