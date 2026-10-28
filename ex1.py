customer_name="Jhansi"
hotel_name="sunshine hotel"
room_price=2000
number_of_days=3
gst_rate=18
total_price=room_price*number_of_days
gst_amount=total_price*gst_rate/100
final_amount=total_price+gst_amount
print(f"Customer Name: {customer_name}\nHotel Name: {hotel_name}\nRoom Price: {room_price}\nNumber of Days: {number_of_days}\nTotal Price: {total_price}\nGST Amount: {gst_amount}\nFinal Amount: {final_amount}")

print("booking successful!")
