import sys
import os
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest



class PayPalClient:
    def __init__(self):
        self.client_id = os.environ.get('PAYPAL_CLIENT_ID')
        self.client_secret = os.environ.get('PAYPAL_SECRET_KEY')

        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key,value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                        self.object_to_json(value) if not self.is_primittive(value) else\
                         value
        return result
    
    def array_to_json_array(self, json_array):
        result =[]
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if  not self.is_primittive(item) \
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, int)


class GetOrder(PayPalClient):
    def get_order(self, order_id):
        request = OrdersGetRequest(order_id)
        response = self.client.execute(request)
        print('Status Code: ', response.status_code)
        print('Status: ', response.result.status)
        print('Order ID: ', response.result.id)
        print('Intent: ', response.result.intent)
        print('Links:')
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print('Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                            response.result.purchase_units[0].amount.value))
        return response

    def capture_order(self, order_id, debug=False):
        request = OrdersCaptureRequest(order_id)
        response = self.client.execute(request)
        if debug:
            print('Status Code: ', response.status_code)
            print('Status: ', response.result.status)
            print('Order ID: ', response.result.id)
            print('Links: ')
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        
        print('Capture Ids: ')
        for purchase_unit in response.result.purchase_units:
            for capture in purchase_unit.payments.captures:
                print('\t', capture.id)
        print("Buyer:")
        print("\tEmail Address: {}\n\tName: {}".format(response.result.payer.email_address,
            response.result.payer.name.given_name + " " + response.result.payer.name.surname))
        return response
