# driver_name = "Parthasarathy G"

# mobile_number = "9876543210"
# blurred = mobile_number[:2] + "XXXXXX" + mobile_number[-2:]
# print(f"Driver {driver_name} can be contacted at {blurred}")


# song = "I wanna BE yours"
# artist = "Arctic Monkeys"
# format=f"{song.title()} - {artist.title()}"

# print(format)

# location = "Coimbatore"
# fixed_location =location.replace("Coimbatore", "Kovai")
# print(fixed_location)

message = "Your uber id is : UBR12345. Please keep it safe."
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id)