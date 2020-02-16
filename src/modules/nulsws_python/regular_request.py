#!/usr/bin/python3.7

import json
from asyncio import sleep as a_sleep
import src.modules.nulsws_python.routines as routines


class RegularRequest(object):

    async def regular_request_m(self, websock_conn, j_reg_dict):
        pause_time = .7
        str_msg_out = "\n* * * REGULAR message going out: \n"
        str_msg_rec = "   -----------> ! ! ! REGULAR response received: "
        str_msg_end = "-----------end previous / begin next request-------------------"

        routines_obj = routines.Routines()
        json_reg = json.dumps(j_reg_dict)
        routines_obj.print_json_request(json_reg, str_msg_out)

        await websock_conn.write_message(json_reg)  # 2 WRITE

        read_reg = await websock_conn.read_message()  # 3 READ
        await a_sleep(pause_time)

        if len(read_reg) > 0:
            routines_obj.print_json_request(read_reg, str_msg_rec)

        routines_obj.myprint(str_msg_end)
        a = 1
