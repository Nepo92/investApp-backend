import graphene
from data import db_connect

class User(graphene.ObjectType):
    id = graphene.Int()
    firstname = graphene.String()
    lastname = graphene.String()
    login = graphene.String()
    password = graphene.String()
    age = graphene.Int()

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        connect = db_connect.connectToDB()
        cursor = connect.cursor()
        
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        cursor.close()
        connect.close()

        response = []

        for user in users:
            response.append(User(
                id = user[0],
                firstname = user[1],
                lastname = user[2],
                login = user[3],
                password = user[4],
                age = user[5])
            )            

        return response
    
user_schema = graphene.Schema(query=Query)