def create_profile(**kwargs):
    print("User Profile")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

create_profile(name = "Parthasarathy", age = "23", job = "Software Engineer")