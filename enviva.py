import os

print("The keys and values of all enviroment varaibles are:")
for key in os.environ:
    print(key, '=>', os.environ[key])

print("The values of home enviroment varaibles are:", os.environ['HOME'])

print(os.getenv('beatifulsoup4'))