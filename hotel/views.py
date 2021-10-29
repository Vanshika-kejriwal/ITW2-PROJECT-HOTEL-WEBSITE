from django.shortcuts import render
from django.http import HttpResponse
from .forms import customer_registration, cancel_booking
from .models import costomer, Rooms
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    return render(request, 'index.html') 

def booking(request):
    if request.method == 'POST':
        fm = customer_registration(request.POST)
        if fm.is_valid():
           fm.save()
           room_req = costomer.objects.latest('id')
           room_avl = Rooms.objects.filter(room_type=room_req.RoomCategory)
           for room in room_avl:
               if room.status == 'free':
                   room_avl.update(status='occupied')
                   messages.success(request, "Room has been booked successfully")
                   break 
               else:
                   room_booked = costomer.objects.filter(RoomCategory=room_req.RoomCategory)
                   for room in room_booked:
                       if room_req.CheckIN>room.CheckOUT or room_req.CheckIN<room.CheckIN:
                           room_avl.update(status='occupied')
                           messages.success(request, "Room has been booked successfully")
                           break
                       else:
                           messages.error(request, "No room available in the selected category. Please choose another category of rooms.")

    else:
        fm = customer_registration() 
    return render(request,'booking.html', {'form':fm})

def cancel(request):
    if request.method == 'POST':
      f1 = cancel_booking(request.POST)
      if f1.is_valid():
         nm = request.POST.get('name')
         ph = request.POST.get('Phone')
         chk_in = request.POST.get('CheckIN')
         chk_out = request.POST.get('CheckOUT')
         rm_cat = request.POST.get('room_catagory')        
         del_cust = costomer.objects.filter(name=nm , Phone=ph, CheckIN=chk_in, CheckOUT=chk_out,RoomCategory=rm_cat)
         chk_in_date = datetime.strptime(chk_in, '%Y-%m-%d')
         dcurrent = datetime.today()
         dt = dcurrent.date() - chk_in_date.date()
         if len(del_cust)==0:
             messages.error(request, 'please enter correct details to cancel booking')
         elif len(del_cust)!=0 and dt.days>1:
             messages.error(request, 'bookings can be cancelled only 24 hours before the check in date.')
             del_cust.delete()
             rs = Rooms.objects.filter(room_type=rm_cat)
             for i in rs:
                 rs.update(status='free')
                 break
         else:
             del_cust.delete()
             rs1 = Rooms.objects.filter(room_type=rm_cat)
             for i in rs1:
                 rs1.update(status='free')
                 break
             messages.success(request, 'Your booking has been cancelled successfully') 
    else:
        f1 = cancel_booking()
    return render(request,'cancel.html',{'form':f1})

def dining(request):
    return render(request, 'dining.html')




      