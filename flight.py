# class flight():
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.passenger=[]
#     def add_passenger(self,name):
#         if not self.openseat():
#             return False
#         self.passenger.append(name)
#         return True
#     def openseat(self):
#         return self.capacity-len(self.passenger)

# flight = flight(3)
# people = ["Ram","Shyam","Hari","Depak"]
# for person in people:
#     if  flight.add_passenger(person):
#         print(f"{person} has sucessfully boarded in flight")
#     else:
#         print(f"{person} has nt boarded")