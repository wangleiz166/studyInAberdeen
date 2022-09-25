#编写一个程序，询问用户年薪，然后显示税前月薪（20%）和税后月薪
year_salary = int(input("enter year salar"))

m_salary_first_value = year_salary/12

m_salary_value = m_salary_first_value*0.8

print(f"your monthly salary is {m_salary_first_value} and  before tax is {m_salary_value}")

