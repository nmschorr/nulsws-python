from Libraries.Constants.nulsws_CONSTANTS_API_LABELS import *
from Libraries.Constants.nulsws_CONSTANTS_PARAM_LABELS import *
from UserSettings.nulsws_SET import *
from Libraries.Constants.Dictionaires.nulsws_NAME_PAIRS import NAME_PAIRS

from UserSettings.nulsws_USER_PARAMS import USER_CALLS_DB as mydb
mylist = [

[
    AC_EXPORT_ACCOUNT_KEYSTORE, [
        (CHAINID, my_chainid),
        (ADDRESS, my_address),
        (PASSWORD, my_password),
        (FILEPATH, None)
    ]
         ],

    [
    AC_EXPORT_KEYSTORE_JSON, [
        (CHAINID, my_chainid),
        (ADDRESS, my_address),
        (PASSWORD, my_password)
        ]
],
    [
        AC_GET_ACCOUNT_BYADDRESS, [
        (CHAINID, my_chainid),
        (ADDRESS, my_address)
        ]
    ]

]


counter = 4
for item in mydb:
    sunder = "_"
    counter += 1
    api_name_tup = [i for i in NAME_PAIRS if i[1] == item[0]]

    try:
        paramlist = item[1]
    except:
        counter += 1
        break

    if paramlist:

        for param in paramlist:
            caps_name = api_name_tup[0]
            prefix = sunder + str(counter) + sunder
            newbigprefix = prefix + caps_name[0] + sunder
            namelist = []

            for tup in paramlist:
                oldname = tup[0]
                newname = newbigprefix + oldname
                namelist.append((oldname, newname,))

        print("[\n" + caps_name[0] + ", [")
        for name in namelist:
            c = name[0].upper()
            n = name[1].lower()
            m = name[1]
            # if "hash" in n:
            #     print(m + " = my_hash,")

            #     print(m + " = my_hash,")
            # elif "address" in n:
            #     print(m + " = my_address,")
            # elif "password" in n:
            print("(" + c + ", " + m + "),")
            # elif "chainid" in n:
            #     print(m + " = my_chainid,")
            #
            # else:
            #     print(m + " = UNKNOWN,")

        print("]],")
        paramlist.clear()


      # [
      #     AC_CREATE_MULTI_SIGN_TRANSFER, [  #4
      #     (CHAINID, _4AC_CREATE_MULTI_SIGN_ACCOUNT_chainid),
      #     (INPUTS, _4AC_CREATE_MULTI_SIGN_ACCOUNT_inputs),
      #     (OUTPUTS, _4AC_CREATE_MULTI_SIGN_ACCOUNT_outputs),
      #     (REMARK, _4AC_CREATE_MULTI_SIGN_ACCOUNT_remark),
      #     (SIGNADDRESS, _4AC_CREATE_MULTI_SIGN_ACCOUNT_signaddress),
      #     (SIGNPASSWORD, _4AC_CREATE_MULTI_SIGN_ACCOUNT_signpassword)
      # ]],