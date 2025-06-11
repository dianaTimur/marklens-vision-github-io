# countries_and_capitals = [
# ("Afghanistan", "Kabul"),
# ("Albania", "Tirana"),
# ("Algeria", "Algiers"),
# ("Andorra", "Andorra la Vella"),
# ("Angola", "Luanda"),
# ("Antigua and Barbuda", "Saint John's"), ("Argentina", "Buenos Aires"), ("Armenia", "Yerevan"),
# ("Australia", "Canberra"),
# ("Austria", "Vienna"),
# ("Azerbaijan", "Baku"),
# ("Bahamas", "Nassau"),
# ("Bahrain", "Manama"),
# ("Bangladesh", "Dhaka")]

# for index,(name1 , name2) in enumerate(countries_and_capitals):
#     print(f'{index+1}. {name1} : {name2}') #1:37 end


# entences = ['Hello from Codezilla', 'Python Course is awesome', 'I enjoy learning Python with Codezilla']

# new_string = []
# for index, string in enumerate(entences):
#     string = string.upper().replace(' ','-')
#     new_string.append(string)
#     string_all = '-'.join(new_string)
# print(string_all) #7:28 end



books = [
("The 7 Habits of Highly Effective People", "Stephen R.Covey"),
("How to Win Friends and Influence People", "DaleCarnegie"),
("Atomic Habits", "James Clear"),
("The 4-Hour Work Week", "Tim Ferriss"),
("Deep Work", "Cal Newport"),
("So Good They Can't Ignore You", "Cal Newport"), 
("Digital Minimalism", "Cal Newport")]

for index, (book,author) in enumerate(books):
    print(f'{index+1}. Book : {book} - Author : {author}') # 2:30 end
    


