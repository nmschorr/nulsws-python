import json

a =  {"MessageID": "6829373212746682", "Timestamp": "1575682937321", "TimeZone": "8", "MessageType": "Request", "MessageData": {"RequestType": "3", "SubscriptionEventCounter": "0", "SubscriptionPeriod": "1", "SubscriptionRange": "0", "ResponseMaxSize": "0", "RequestMethods": [{"GetBalance": {"Address": "NULSd6HghM9Z9XytwZEHGDGRJLnNR5ybiy5gt"}}, {"GetHeight": {}}]}}

print(json.dumps(a, indent=4))


