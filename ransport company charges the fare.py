

# Function to calculate the transport fare based on distance
def calculate_fare(distance):
    if 1 <= distance <= 50:
        fare = distance * 8
    elif 51 <= distance <= 100:
        fare = distance * 10
    elif distance > 100:
        fare = distance * 12
    else:
        fare = 0  # Assuming no fare for distances less than 1 KM
    return fare

# Input the distance from the user
distance = float(input("Enter the distance traveled in KM: "))

# Calculate the fare
fare = calculate_fare(distance)

# Display the result
print(f"The transport fare for {distance} KM is: Rs. {fare:.2f}")
