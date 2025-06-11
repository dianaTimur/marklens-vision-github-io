user_name = input('Enter your name:').capitalize().strip()
company_name = input('Enter your company name:').capitalize().strip()
birth = input('Enter your birth year:')
email  = input('Enter your email : ')

indx_name = user_name.index(" ")

frist_3_company = company_name[:3]

list_2_name = user_name[-2:]

indx_email = email.index("@")

email = email[:indx_email]

id = f"Your id is : {frist_3_company.lower()}-{list_2_name}{birth}\nAnd your email is : {email}@{company_name.lower()}.com"
print(f"Hello {user_name[:indx_name]}\nWelcome at {company_name}")
print(id)


