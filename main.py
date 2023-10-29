import pandas

df = pandas.read_csv('005 hotels.csv',dtype={'id':str})
df_cards = pandas.read_csv('cards.csv',dtype=str).to_dict(orient='records')
df_card_security = pandas .read_csv('card-security.csv',dtype =str)
class Hotel:

    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id,'name'].squeeze()

    def book(self):
        df.loc[df['id'] == self.hotel_id,'available'] = 'no'
        df.to_csv('005 hotel.csv',index=False)
        pass

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id,'available'].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class SpaHotel(Hotel):
    def book_spackage(self):
        pass


class Reservation:
    def __init__(self,customer_name,hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content= f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Home name : {self.hotel.name}
        
"""
        return content

class Creditcard:
    def __init__(self,number):
        self.number = number

    def validate(self,expiration,holder,cvc):
        card_data ={'credit_number':self.number,'expiration':expiration,
                    'holder':holder,'cvc':cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(Creditcard):
    def check_security(self,password):
        card_security = df_card_security.loc[df_card_security['number']==self.number,'password'].squeeze()
        if card_security ==password:
            return True
        else:
            return False

class SpaReservation:
    def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"""
         Thank you for your Spareservation!
        Here are your booking data:
        Name: {self.customer_name}
        Home name : {self.hotel_object}
        
"""





print(df)
hotel_ID = input('Enter the id of the hotel: ')


hotel = SpaHotel(hotel_ID)
if hotel.available():
    """Check if the hotel is available"""

    number = input('Enter a number: ')
    expiration = input('Enter the exp number: ')
    cvc = input('Enter a cvc number: ')
    holder =input('Enter the exact name on the card:')

    credit_card = SecureCreditCard(number=number)
    if credit_card.validate(expiration=expiration,cvc=cvc,holder=holder):
        passcode = input('Enter your passcode: ')
        if credit_card.check_security(password=passcode):
            hotel.book()
            name = input('Enter your name: ')
            reservation_ticket = Reservation(customer_name= name,hotel= hotel)
            print(reservation_ticket.generate())
            spa_package = input('Do you want  to book a spa_package? ')
            spaR = SpaReservation(customer_name=name,hotel_object=hotel)
            if spa_package == 'yes':
                print(spaR.generate())

        else:
            print('Credit card authentication failed')
    else:
        print('there was problem with the payment method')
else:
    print('Hotel is not available')