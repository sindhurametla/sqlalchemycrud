from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, VARCHAR
import os

load_dotenv()

DATABASE_URL = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DATABASE')}"
engine =create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autoflush = False, autocommit = False, bind = engine)
db = sessionLocal()
Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id  = Column(Integer, primary_key = True, index = True)
    name = Column(VARCHAR(255))
    age = Column(Integer)

    def __repr__(self):
        return f"id = {self.id}, name = {self.name}, age = {self.age}"
        #return f"<User(id = {self.id}, name = {self.name}, age = {self.age})>"

Base.metadata.create_all(bind = engine)

#to add users into the table to avoid duplicate entries
def add_user():
    user_name = input("Enter your name:")
    user_age = int(input("Enter your age:"))
    existing_user = db.query(Users).filter(Users.name == user_name).first()
    if not existing_user:
        new_user = Users(name = user_name, age = user_age)
        db.add(new_user)
        print("user added successfully")
        db.commit()
    else:
        print("user already exists")



#to get all users in the table
def getall_users():
    all_users = db.query(Users).all()
    for user in all_users:
        print(user)


# to update the user
def update_user():
    user_id = int(input("Enter the id:"))
    user_name = input("Enter the name to update:")
    user_age = int(input("Enter the age to update:"))
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        user.name = user_name
        user.age = user_age
        print("user updated successfully")
        db.commit()
    else: 
        print("user not found")


def delete_user():
    del_user = input("Enter the name to delete:")
    user = db.query(Users).filter(Users.name == del_user).first()
    if user:
        db.delete(user)
        db.commit()
        print("user deleted successfully")
    else: 
        print("user not found")
       


#to perform user choice operation
choice = input("Enter your choice(ex:add/update):")
if choice == "add":
    add_user()
elif choice == "update":
    update_user()
elif choice == "getusers":
    getall_users()
elif choice == "delete":
    delete_user()