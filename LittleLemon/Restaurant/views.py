from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from utils import *
from Restaurant.models import *
from Restaurant.serializers import *
from utils import dictfetchall as dictfetchall
from django.http import HttpResponse
# Create your views here.

class BookingCRUD(APIView):

    def get(self, request, recno = None):
        success = False          # Boolean for Success 

        try:
            if recno:
                get = 'SELECT * FROM booking WHERE id = %s'
                with connection.cursor() as c:
                    c.execute(get, [recno])
                    row = dictfetchall(c)
                success = True
            else:
                get = 'SELECT * FROM booking'
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)
                success = True

                return Response({'Success' : success, 'Message' : row}, status=200)
            
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)
        


    def post(self, request):
        serializer = bookingserializer(data=request.data)
        success = False
        try:
            if serializer.is_valid():
                serializer.save()  # Save the validated data as a new Booking instance
                latest_booking = Booking.objects.latest('id')  # Get the latest booking

                response_data = {
                    'Success': True,
                    'Message': bookingserializer(latest_booking).data
                }
                return Response(response_data, status=200)
            else:
                return Response({'Success': False, 'Error': serializer.errors}, status=400)

         
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)
        

    
    def patch(self, request):

        success = False
        try:
            request_data = request.data
            id = request_data['id']

            try:
                booking_obj = Booking.objects.get(id = id)
            except:
                raise Exception({'Success' : 'False', 'Error' : 'Not Found'})
        
    
            name = request_data.get('name', booking_obj.name)
            noOfGuests = request_data.get('noOfGuests', booking_obj.noOfGuests)
            booking_date = request_data.get('booking_date', booking_obj.booking_date)

            update = 'UPDATE booking SET name = %s, noOfGuests = %s, booking_date = %s WHERE id = %s'
            with connection.cursor() as c:
                c.execute(update, [name, noOfGuests, booking_date, id])
            success = True
            return Response({'Success': success, 'Message': 'Updated Successfully'}, status=200)

            
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : 'False', 'Error' : str(err)}, status=400)
        



class MenuCRUD(APIView):

    def get(self, request, recno = None):
        success = False          # Boolean for Success 

        try:
            if recno:
                get = 'SELECT * FROM menu WHERE id = %s'
                with connection.cursor() as c:
                    c.execute(get, [recno])
                    row = dictfetchall(c)
                success = True
            else:
                get = 'SELECT * FROM menu'
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)
                success = True

                return Response({'Success' : success, 'Message' : row}, status=200)
            
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)
        
    def post(self, request):
        serializer = menuserializer(data=request.data)
        success = False
        try:
            if serializer.is_valid():
                serializer.save()  # Save the validated data as a new Booking instance
                latest_menu = Menu.objects.latest('id')  # Get the latest booking

                response_data = {
                    'Success': True,
                    'Message': menuserializer(latest_menu).data
                }
                return Response(response_data, status=200)
            else:
                return Response({'Success': False, 'Error': serializer.errors}, status=400)

         
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)
        

    
    def patch(self, request):

        success = False
        try:
            request_data = request.data
            id = request_data['id']

            try:
                menu_obj = Menu.objects.get(id = id)
            except:
                raise Exception({'Success' : 'False', 'Error' : 'Not Found'})
        
    
            title = request_data.get('title', menu_obj.title)
            price = request_data.get('price', menu_obj.price)
            inventory = request_data.get('inventory', menu_obj.inventory)

            update = 'UPDATE menu SET title = %s, price = %s, inventory = %s WHERE id = %s'
            with connection.cursor() as c:
                c.execute(update, [title, price, inventory, id])
            success = True
            return Response({'Success': success, 'Message': 'Updated Successfully'}, status=200)

            
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : 'False', 'Error' : str(err)}, status=400)