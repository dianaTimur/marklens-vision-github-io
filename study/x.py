# contacts =[
#              ('Amira Abdelrahman', '+1-555-555- 5556', 'amiraabdelrahman@example.com'),
#                ('Abdullah Othman', '+1-555-555-5557', 'abdullahothman@example.com'),
#                  ('Ahmed Saeed', '+1-555-555-5558', 'ahmedsaeed@example.com'), 
#                  ('Saleh Abdelhamid', '+1-555-555-5559', 'salehabdelhamid@example.com'), 
#                  ('Fatima Ali', '+1-555-555-5560', 'fatimaali@example.com'), 
#                  ('Omar Hasan', '+1-555-555-5561', 'omarhasan@example.com'), 
#                  ('Aisha Ahmed', '+1-555-555-5562', 'aishaahmed@example.com'),
#              ('Karim Hassan', '+1-555-555-5563', 'karimhassan@example.com')]


# # for all in contacts:
# #     name,phone,email = all
# #     print(f'Name: {name}\nPhone Number : {phone}\nEmail : {email} ')
# #     print('-' * 15)

# # grocery_name = ['apple','banana','orange','grapes','tomato',
# #                 'potato','milk','bread','butter','asa']

# # grocery_prices = [0.99, 0.50 , 0.75,2.99,1.49,0.99,3.99,2.49,4.99]

# # masseg = """ 
# # Gorcery List :
# # Item             Price
# # -------------------------
# # """
# # print(f'{masseg} ')
# # for i in range(len(grocery_name)):
# #     if  i < len(grocery_name):
# #         all = (f"{grocery_name[i]}\t\t${grocery_prices[i]:.2f}")
# #         print(all)




# contacts = [
# ("Mohamed Gouda", "+1-555-555-5555",
# "mohamedgouda@example.com"),
# ("Amira Abdelrahman", "+1-555-555-5556",
# "amiraabdelrahman@example.com"), 
# ("Abdullah Othman", "+1-555-555-5557",
# "abdullahothman@example.com"), 
# ("Ahmed Saeed", "+1-555-555-5558",
# "ahmedsaeed@example.com"),
# ("Saleh Abdelhamid", "+1-555-555-5559",
# "salehabdelhamid@example.com"),
# ("Fatima Ali", "+1-555-555-5560", "fatimaali@example.com"),
#  ("Omar Hasan", "+1-555-555-5561", "omarhasan@example.com"), 
#  ("Aisha Ahmed", "+1-555-555-5562",
# "aishaahmed@example.com"),
# ("Karim Hassan", "+1-555-555-5563",
# "karimhassan@example.com")
# ]


# while True:

#   for name,phone,email in contacts:
#      pass
    
#   choace = input ('''Welcome to the phonebook appliction ! 

#   Enter your choace
                   
#   1. app a contact 
#   2. update a contact 
#   3. search for a contact
#   4. Quit     
#   ''')
  
#   if choace == '1':
#     NewName = input('Enter name : ').title()
#     NewPhone = input('Enter phone : ')
#     NewEmail = input('Enter Email : ')
#     contacts.append((NewName,NewPhone,NewEmail))
#     name = contacts
#   elif choace == '2':
#     LookingName = input('Enter name of the contact you want to update : ').title()
#     IndexName = name.index(' ')
#     if LookingName in name[:IndexName]:
#         NewPhone = input('Enter new Phone : ')
#         NewEmail = input('Enter new Email : ')
    
#         print('Contact update successfully ! ')
#     else:
#         print('This name is not found  . ')
#   elif choace == '3':
#     SearchName = input('Enter name of contact you want to search : ').title()
#     IndexName = name.index(' ')
#     if SearchName in name[:IndexName]:
#       phone,email = NewPhone,NewEmail
#       print(f'Name : {name}')
#       print(f'Phone : {phone}')
#       print(f'Email : {email}')
#     else:
#        print('Is not found . ')
#   elif choace == '4':
#      print('Bye')
#      break
#   else:
#      print('Plasae Enter 1,2,3,4')



countries = [('Palestine', 'Al-Quds', 'Asia', 'Arabic', 5000000), ('Algeria', 'Algiers', 'Africa', 'Arabic', 42000000), ('Bahrain', 'Manama', 'Asia', 'Arabic', 1700000), ('Comoros', 'Moroni', 'Africa', 'Arabic', 800000),
('Djibouti', 'Djibouti', 'Africa', 'Arabic', 900000), ('Egypt', 'Cairo', 'Africa', 'Arabic', 100000000), ('Iraq', 'Baghdad', 'Asia', 'Arabic', 40000000),
('Jordan', 'Amman', 'Asia', 'Arabic', 10000000), ('Kuwait', 'Kuwait City', 'Asia', 'Arabic', 4000000), ('Lebanon', 'Beirut', 'Asia', 'Arabic', 6000000),
('Libya', 'Tripoli', 'Africa', 'Arabic', 7000000), ('Morocco', 'Rabat', 'Africa', 'Arabic', 35000000), ('Oman', 'Muscat', 'Asia', 'Arabic', 5000000), 
('Qatar', 'Doha', 'Asia', 'Arabic', 2700000), ('Saudi Arabia', 'Riyadh', 'Asia', 'Arabic', 34000000), ('Sudan', 'Khartoum', 'Africa', 'Arabic', 43000000),
('Syria', 'Damascus', 'Asia', 'Arabic', 17000000), ('Tunisia', 'Tunis', 'Africa', 'Arabic', 11000000), ('United Arab Emirates', 'Abu Dhabi', 'Asia', 'Arabic', 10000000), 
('Yemen', "Sana'a", 'Asia', 'Arabic', 29000000), ('Indonesia', 'Jakarta', 'Asia', 'Indonesian', 2700000000), ('Pakistan', 'Islamabad', 'Asia', 'Urdu', 2200000000), ('Bangladesh', 'Dhaka', 'Asia', 'Bengali', 1600000000),
('Turkey', 'Ankara','Europe/Asia', 'Turkish', 80000000),
('Iran', 'Tehran', 'Asia', 'Persian', 83000000), ('Malaysia', 'Kuala Lumpur', 'Asia', 'Malaysian', 32000000), ('Nigeria', 'Abuja', 'Africa', 'English', 200000000),
('Ethiopia', 'Addis Ababa', 'Africa', 'Amharic', 110000000), ('Albania', 'Tirana', 'Europe', 'Albanian', 2877797), ('Andorra', 'Andorra la Vella', 'Europe', 'Catalan', 77006), 
('Austria', 'Vienna', 'Europe', 'German', 8955102), ('Belarus','Minsk', 'Europe', 'Belarusian', 9449323), ('Belgium', 'Brussels', 'Europe', 'Dutch, French, German', 11519193),
('Bosnia and Herzegovina', 'Sarajevo', 'Europe', 'Bosnian, Serbian, Croatian', 3280819), ('Bulgaria', 'Sofia', 'Europe', 'Bulgarian', 6948445), ('Croatia', 'Zagreb', 'Europe', 'Croatian', 4105267), 
('Cyprus', 'Nicosia', 'Europe', 'Greek, Turkish', 1189265), ('Czech Republic', 'Prague', 'Europe', 'Czech', 10618303), ('Denmark', 'Copenhagen', 'Europe', 'Danish', 5792202), ('Estonia', 'Tallinn', 'Europe', 'Estonian', 1324333), 
('Finland', 'Helsinki', 'Europe', 'Finnish, Swedish', 5540720), ('France', 'Paris', 'Europe', 'French', 67102172), ('Germany', 'Berlin', 'Europe', 'German', 82979224), ('Greece', 'Athens', 'Europe', 'Greek',
10423054), ('Hungary', 'Budapest', 'Europe', 'Hungarian', 9769526), ('Iceland', 'Reykjavik', 'Europe', 'Icelandic', 341243), ('Ireland', 'Dublin', 'Europe', 'English, Irish', 4761657), 
('Italy', 'Rome', 'Europe', 'Italian', 60461826), ('Kosovo', 'Pristina', 'Europe', 'Albanian, Serbian', 1800000), ('Latvia', 'Riga', 'Europe', 'Latvian', 1886198), ('Liechtenstein', 'Vaduz', 'Europe', 'German', 38375), 
('Lithuania', 'Vilnius', 'Europe', 'Lithuanian', 2722289), ('Luxembourg', 'Luxembourg', 'Europe', 'Luxembourgish, French, German', 625978), ('Malta', 'Valletta', 'Europe', 'Maltese, English', 514000), ('Moldova', 'Chisinau', 'Europe', 'Romanian', 2883300),
('Monaco', 'Monaco', 'Europe', 'French', 39242), ('Montenegro', 'Podgorica', 'Europe', 'Montenegrin', 621810), ('Netherlands', 'Amsterdam', 'Europe', 'Dutch', 17231017), ('North Macedonia', 'Skopje', 'Europe', 'Macedonian', 2083374), ('Canada', 'Ottawa', 'North America', 'English, French', 38550000),
('United States', 'Washington, D.C.', 'North America', 'English', 329000000), ('Mexico', 'Mexico City', 'North America', 'Spanish', 130750000), ('Brazil', 'Brasília', 'South America', 'Portuguese', 211200000), ('Argentina', 'Buenos Aires', 'South America', 'Spanish', 44480000), 
('Colombia', 'Bogotá', 'South America', 'Spanish', 50370000), ('Peru', 'Lima', 'South America', 'Spanish', 32160000), ('Venezuela', 'Caracas', 'South America', 'Spanish', 28200000)]



input_name = input('Enter a country name or capital to search : ').title()

for i in countries:
    if input_name in i :
        print('Here are the result : ')
        print('-----------')
        print(f'country : {i[0]}')
        print(f'capital : {i[1]}')
        print(f'continent : {i[2]}')
        print(f'language : {i[3]}')
        print(f'population : {i[-1]:,}')
    else:
      print('is not here')