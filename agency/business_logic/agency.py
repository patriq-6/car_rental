from .car_list import CarList
from .driver_list import DriverList
from .booking_log import BookingLog
from .rental_log import RentalLog
from .invoice_log import InvoiceLog
from .payment_log import PaymentLog
class Agency:
    def __init__(self):
        self.cars = CarList()
        self.drivers = DriverList()
        self.bookings = BookingLog()
        self.rentals = RentalLog()
        self.invoices = InvoiceLog()
        self.payments = PaymentLog()

    def add_car(self,car_model,reg_no,color,fuel,fare,image):
        self.cars.add_car(car_model,reg_no,color,fuel,fare,image)

    def delete_car(self,reg_no):
        return self.cars.delete_car(reg_no)

    def update_car(self,searched_car,color,fuel,image,fare,accident_details):
        self.cars.update_car(searched_car,color,fuel,image,fare,accident_details)

    def add_driver(self,CNIC,first_name,last_name,email,contact_number,address,hourly_rate):
        self.drivers.add_driver(CNIC,first_name,last_name,email,contact_number,address,hourly_rate)

    def delete_driver(self,CNIC):
        return self.drivers.delete_driver(CNIC)

    def update_driver(self,CNIC,first_name,last_name,email,contact_number,address,hourly_rate):
        self.drivers.update_driver(CNIC,first_name,last_name,email,contact_number,address,hourly_rate)

    def book_car(self,customer,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed):
        return self.bookings.create_booking(customer,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed)

    def receive_car(self,booking,date_of_delivery):
        self.rentals.create_rental(booking,date_of_delivery)

    def create_invoice(self,booking_id):
        return self.invoices.create_invoice(booking_id)

    def delete_invoice(self,invoice_id):
        return self.invoices.delete_invoice(invoice_id)

    def make_payment(self,booking_id,amount,payment_date,credit_card=None):
        self.payments.create_payment(booking_id,amount,payment_date,credit_card)
