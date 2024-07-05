#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Password_Manager:
    def __init__(self,web_app,desk_app,game):
        self.web_app = web_app
        self.desk_app = desk_app
        self.game_app = game
    def web_application(self):
        user_input = input("Please enter the type of aplication for which you want to store data: ")
        if user_input == "Web Application":
            import mysql.connector
            mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
            mycursor = mydb.cursor()
            sql = "INSERT INTO website_passwords (username, web_password, website_name, website_url, created_data, last_updated_date) VALUES (%s, %s, %s, %s, %s, %s)"
            storage_data = []
            storage_username = input("Please enter your username: ")
            storage_data.append(storage_username)
            storage_password = input("Please enter your Password: ")
            from cryptography.fernet import Fernet

            key = Fernet.generate_key()

            key_object = Fernet(key)
            encrypted_password = key_object.encrypt(storage_password.encode())
            storage_data.append(encrypted_password)
            storage_websitename = input("Please enter your Website Name: ")
            storage_data.append(storage_websitename)
            storage_url = input("Please enter your Website URL: ")
            storage_data.append(storage_url)
            storage_created_data = input("Please enter your Created Date: ")
            storage_data.append(storage_created_data)
            storage_updated_date = input("Please enter your Updated Date: ")
            storage_data.append(storage_updated_date)
            mycursor.execute(sql, storage_data)
            mydb.commit()
            print(mycursor.rowcount, "Inserted Records")
        else:
            print("Plaese enter a Web Application to Access this functionality")
    def web_application_records(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM website_passwords")
        web_result = mycursor.fetchall()
        for x in web_result:
            print(x)
    def web_application_update(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
        mycursor = mydb.cursor()

        sql = "UPDATE website_passwords SET web_password = %s WHERE user_id = %s"
        update_data = []
        new_password = input("Please enter new password: ")
        update_data.append(new_password)
        password_id = int(input("Enter user_id"))
        update_data.append(password_id)
        mycursor.execute(sql, update_data)
        mydb.commit()
    def web_application_delete_records(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
        mycursor = mydb.cursor()
        sql = "DELETE FROM website_passwords WHERE user_id = %s;"
        user_delete_id = []
        user_delete_input = int(input("Please enter the user_id to delete that record: "))
        user_delete_id.append(user_delete_input)
        mycursor.execute(sql, user_delete_id)
        mydb.commit()
    def desktop_application(self):
        user_input = input("Please enter the type of aplication for which you want to store data: ")
        if user_input == "Desktop Application":
            import mysql.connector
            mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
            mycursor = mydb.cursor()
            sql = "INSERT INTO desktop_passwords (username, app_password, app_name, created_data, last_updated_date) VALUES (%s, %s, %s, %s, %s)"
            storage_data = []
            storage_desktop_username = input("Please enter your username: ")
            storage_data.append(storage_desktop_username)
            storage_deskttop_password = input("Please enter your Password: ")
            from cryptography.fernet import Fernet

            key = Fernet.generate_key()

            key_object = Fernet(key)
            encrypted_password = key_object.encrypt(storage_deskttop_password.encode())
            storage_data.append(encrypted_password)
            storage_desktopname = input("Please enter your Desktop Application Name: ")
            storage_data.append(storage_desktopname)
            storage_created_data = input("Please enter your Created Date: ")
            storage_data.append(storage_created_data)
            storage_updated_date = input("Please enter your Updated Date: ")
            storage_data.append(storage_updated_date)
            mycursor.execute(sql, storage_data)
            mydb.commit()
            print(mycursor.rowcount, "Inserted Records")
        else:
            print("Plaese enter a Desktop Application to access this functionality")
    def desktop_application_records(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM desktop_passwords")
        web_result = mycursor.fetchall()
        for x in web_result:
            print(x)
    def desktop_application_update(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
        mycursor = mydb.cursor()

        sql = "UPDATE desktop_passwords SET app_password = %s WHERE user_id_desktop = %s"
        update_data = []
        new_password = input("Please enter new password: ")
        update_data.append(new_password)
        password_id = int(input("Enter user_id"))
        update_data.append(password_id)
        mycursor.execute(sql, update_data)
        mydb.commit()
    def desktop_application_delete_records(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
        mycursor = mydb.cursor()
        sql = "DELETE FROM desktop_passwords WHERE user_id_desktop = %s;"
        user_delete_id = []
        user_delete_input = int(input("Please enter the user_id to delete that record: "))
        user_delete_id.append(user_delete_input)
        mycursor.execute(sql, user_delete_id)
        mydb.commit()
    def game(self):
        user_input = input("Please enter the type of aplication for which you want to store data: ")
        if user_input == "Game":
            import mysql.connector
            mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
            mycursor = mydb.cursor()
            sql = "INSERT INTO game_passwords (username, game_password, game_name,game_developer, created_data, last_updated_date) VALUES (%s, %s, %s, %s, %s, %s)"
            storage_data = []
            storage_game_username = input("Please enter your Game username: ")
            storage_data.append(storage_game_username)
            storage_game_password = input("Please enter your Password: ")
            from cryptography.fernet import Fernet

            key = Fernet.generate_key()

            key_object = Fernet(key)
            encrypted_password = key_object.encrypt(storage_game_password.encode())
            storage_data.append(encrypted_password)
            storage_game_name = input("Please enter your Game Name: ")
            storage_data.append(storage_game_name)
            storage_game_developer = input("Please enter your Game Developer: ")
            storage_data.append(storage_game_developer)
            storage_created_data = input("Please enter your Created Date: ")
            storage_data.append(storage_created_data)
            storage_updated_date = input("Please enter your Updated Date: ")
            storage_data.append(storage_updated_date)
            mycursor.execute(sql, storage_data)
            mydb.commit()
            print(mycursor.rowcount, "Inserted Records")
        else:
            print("Plaese enter a Web Application to Access this functionality")
    def game_records(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM game_passwords")
        web_result = mycursor.fetchall()
        for x in web_result:
            print(x)
    def game_update(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
        mycursor = mydb.cursor()

        sql = "UPDATE game_passwords SET game_password = %s WHERE user_id_game = %s"
        update_data = []
        new_password = input("Please enter new password")
        update_data.append(new_password)
        password_id = int(input("Enter user_id: "))
        update_data.append(password_id)
        mycursor.execute(sql, update_data)
        mydb.commit()
    def game_delete_records(self):
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",password="Iampaul57",
                                           database="password_manager")
        mycursor = mydb.cursor()
        sql = "DELETE FROM game_passwords WHERE user_id_game = %s;"
        user_delete_id = []
        user_delete_input = int(input("Please enter the user_id to delete that record: "))
        user_delete_id.append(user_delete_input)
        mycursor.execute(sql, user_delete_id)
        mydb.commit()


# In[10]:


pp = Password_Manager("yes","yes","yes")


# In[11]:


pp.web_application()


# In[14]:


pp.web_application_records()


# In[13]:


pp.web_application_delete_records()


# In[ ]:




