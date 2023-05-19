# Variables

string_variable = "My string variable"
print(string_variable)

int_variable = 10
print(int_variable)

bool_variable = True
print(bool_variable)

print(string_variable,int_variable,bool_variable)
print(string_variable,str(int_variable),bool_variable)

# Algunas funciones de sistema

print(len(string_variable))

# Variables en una sola línea
name, surname, alias, age ="Cristhian","Araya","Endeken",35
print(f'Me llamo {name} {surname}, mi alias es {alias} y mi edad es {age}')


# Inputs
first_name = input('¿Cúal es tu nombre?: ')
age = input('¿Que edad tienes?: ')


print(first_name, age)

# Cambiamos tipo
age = "Mercurio"
name = 58

print(age, name)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address=True
address=5.2
address=100
print(address)
print(type(address))