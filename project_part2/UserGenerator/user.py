"""Module to generate ranndom users"""
import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

logging.basicConfig(level = logging.INFO,
                    filename=(BASE_DIR / "user.log"),
                    filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')
fake = faker.Faker()
def get_user() :
    """ Generate a single user :
        
        Returns :
            str : user
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"
    

def get_users(n) :
    """ Generate a multiple users :
        args :
            n (int) : Number of user to generate
        Returns :
            list[str] : users
    """
    logging.info(f"Generating a list of {n} user.")
    return [get_user() for _ in range(n)]


if __name__ == "__main__" :
    user = get_users(5)
    print(user)
