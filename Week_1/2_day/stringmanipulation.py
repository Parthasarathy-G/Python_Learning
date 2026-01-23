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

# message = "Your uber id is : UBR12345. Please keep it safe."
# booking_id = message.split(":")[1].split(".")[0].strip()
# print(booking_id)

# promo = "Use code UBER50 to get 50% off on your next ride."
# if "UBER50" in promo:
#     print("Promo code is valid!")

# name = "  parthasarathy g  "
# initial = "".join([word[0].upper() for word in name.strip().split()])
# print(initial)


word1 = "Hello good monring welcome to the system"
word_count = len(word1.split(""))
print(f"The number of words in the given string is: {word_count}")