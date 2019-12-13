#!/usr/bin/python3.7

type_name_dict: dict = {0: 'None', 1: 'NegotiateConnection',
                        2: 'NegotiateConnectionResponse',
                        3: 'Request', 4: 'Unsubscribe', 5: 'Response', 6: 'Ack',
                        7: 'RegisterCompoundMethod', 8: 'UnregisterCompoundMethod'}

compress_type_label = "CompressionAlgorithm"
compress_rate_label = "CompressionRate"
msg_data_label = "MessageData"
msg_id_label = "MessageID"
msg_type_label = "MessageType"
negotiate_conn_label = "NegotiateConnection"
negotiate_stat_label = 'NegotiationStatus'
negotiate_conn_resp_label = "NegotiateConnectionResponse"
proto_label = "ProtocolVersion"
tmstmp_label = "Timestamp"
tmzone_label = "TimeZone"
request_label = "Request"
request_internalid_label = "RequestInternalID"
request_date_label = "RequestDate"
request_time_label = "RequestTime"
json_seps = (',', ':')

request_type_label = "RequestType"
subscrip_evnt_ct_label = "SubscriptionEventCounter"
subscrip_period_label = "SubscriptionPeriod"
subscriptn_range_label = "SubscriptionRange"
req_methods_label = "RequestMethods"
get_bal_label = "GetBalance"
response_max_size_label = "ResponseMaxSize"
address_label = "Address"
get_height_label = "GetHeight"

ZERO = "0"
ONE = "1"
CHAINID_LABEL = "chainId"

# if you change this file, you must keep this list updated
__ALL__ = [ZERO, ONE, CHAINID_LABEL, compress_rate_label, compress_type_label,
           get_bal_label, get_height_label, json_seps, msg_data_label, msg_id_label,
           msg_type_label, negotiate_conn_label, negotiate_conn_resp_label, negotiate_stat_label,
           proto_label, req_methods_label, request_date_label, request_internalid_label, request_label,
           request_type_label, request_time_label, response_max_size_label,
           subscriptn_range_label, subscrip_evnt_ct_label, subscrip_period_label, tmstmp_label, tmzone_label]