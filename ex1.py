customer_name=input("Enter customer name: ")
hotel_name=input("Enter hotel name: ")
room_type=input("Enter room type: ")
room_price= 2000
number_of_days=int(input("Enter number of days: "))
gst_rate= 10
total_price=room_price*number_of_days
gst_amount=total_price*gst_rate/100
final_amount=total_price+gst_amount
print("Booking Details:")
print(f"Customer Name: {customer_name}\nHotel Name: {hotel_name}\nRoom Type: {room_type}\nRoom Price: {room_price}\nNumber of Days: {number_of_days}\nTotal Price: {total_price}\nGST Amount: {gst_amount}\nFinal Amount: {final_amount}")

print("booking successful!")
