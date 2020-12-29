#!/usr/bin/env python

# -*- *************** -*-
# @File  : apex_efb.py
# @Description : 
# @Author: mql
# @Time  : 2020/12/16 14:55
# -*- *************** -*-


import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import time
from datetime import datetime
from mycolorlog import *

# 电气量参数， 30000+key 为寄存器地址
dict_suffix = {1: 'fault', 3: 'u', 4: 'i', 5: 'p', 6: 'i_a_fd', 7: 'i_b_fd', 8: 'i_c_fd', 9: 'i_a_ct', 10: 'i_a_ct',
               11: 'i_a_ct', 12: 'pf_a_out', 13: 'pf_b_out', 14: 'pf_c_out', 15: 't_a_col', 16: 't_b_col',
               17: 't_c_col',
               18: 'freq_mv', 19: 'u_dc',
               22: 'elec_fd_rcnt',
               25: 'am',
               36: 't_a_amb', 37: 't_b_amb', 38: 't_c_amb', 39: 'i_a_out', 40: 'i_b_out', 41: 'i_c_out',
               42: 'i_r_a_out',
               43: 'i_r_b_out', 44: 'i_r_c_out',
               72: 'elec_rect_rcnt', 75: 'fault_rec'}
# 设备状态及运行模式(按位) 30027
dict_suffix_27 = {0: 'status_off', 1: 'status_on', 2: 'fault', 3: 'status_offline', 4: 'status_em', 5: 'status_standby',
                  8: 'mode_fd', 9: 'mode_svg', 10: 'mode_bidc', 11: 'mode_debug', 12: 'mode_rect', 13: 'mode_fd_prty',
                  14: 'mode_self_insp'}
# 开关接触器状态(按位) 30027
dict_suffix_28 = {0: 'status_dc', 1: 'status_ac', 2: 'status_dscn', 3: 'status_km1', 4: 'status_breaker_a',
                  5: 'status_breaker_b', 6: 'status_breaker_c'}
# 总回馈电量 30020,30021（高16位，低16位）
suffix_fd = 'elec_fd'
# 总整流电量 30045,30046（高16位，低16位）
suffix_rect = 'elec_rect'
# 设备累积运行时间 30073,30074（高16位，低16位）
suffix_runtime = 'run_time'
# 总回馈电量设置 40028,40029（高16位，低16位）
suffix_fd_s = 'elec_fd_s'
# 总整流电量设置 40030,40031（高16位，低16位）
suffix_rect_s = 'elec_rect_s'

# 读写点参数， 40000+key 为寄存器地址
suffix_sp = {1: 'status', 2: 'clock_year', 3: 'clock_month', 4: 'clock_day', 5: 'clock_hour', 6: 'clock_minute',
             7: 'clock_second', 8: 'clock_msec', 23: 'ip1', 24: 'ip2', 25: 'ip3', 26: 'ip4', 27: 'rec_read',
             32: 'u_fd_thsd', 33: 'u_fd_start', 34: 'elec_svg', 35: 'mode'}
# 故障录波参数列表，10001~28001，每个参数2000个
rec_params = ['rec_ac_va', 'rec_ac_vb', 'rec_ac_vc',
              'rec_ac_ia', 'rec_ac_ib', 'rec_ac_ic',
              'rec_dc_i', 'rec_switch', 'rec_dc_v']

# 下发相关
for_write = {'status': 40001, 'u_fd_thsd': 40032, 'u_fd_start': 40033, 'elec_svg': 40034, 'mode': 40035}


class ModbusTCP_apex_efb:

    def __init__(self, host="127.0.0.1", port=502, slave=1, timeout=5, tag_prefix=""):
        self.host = host
        self.port = port
        self.slave = slave
        self.timeout = timeout
        self.tag_prefix = tag_prefix

        self.online = False
        self.fault_rec = 0  # 是否有故障录波 30075	-- 0无；1有
        self.reading_rec = False  # 是否正在读取故障录波数据

    def to_connect(self):
        try:
            # 连接MODBUS TCP 从机
            logger.info("@@@@@@ starting conenct to %s:%d slave-%s ......" % (self.host, self.port, self.slave))
            master = modbus_tcp.TcpMaster(self.host, self.port)
            master.set_timeout(self.timeout)
            master.execute(self.slave, cst.READ_INPUT_REGISTERS, 30001, 1)
            logger.info("@@@@@@ conenct to %s:%d slave-%s SUCCESS" % (self.host, self.port, self.slave))
            self.online = True
            self.master = master
        except Exception as e:
            logger.error("@@@@@@ conenct to %s:%d slave-%s ERROR, %s" % (self.host, self.port, self.slave, e))
            self.online = False
            # 等待5秒重新连接
            time.sleep(5)
            self.to_connect()

    def poll_yc_04(self):
        if self.online and self.master is not None:
            oneRes = self.master.execute(self.slave, cst.READ_INPUT_REGISTERS, 30000, 76, data_format=">" + (76 * "h"))
            logger.debug("@@@@@@ --yc04--30000-- %s:%d slave-%s, int-%s, hex- %s" % (
                self.host, self.port, self.slave, str(oneRes), self.intTupleToHexStr(oneRes)))

            tt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            r_list = []

            # 总回馈电量
            r_list.append({'tag': self.tag_prefix + suffix_fd, 'val': (oneRes[20] << 8 + oneRes[21]), 'time': tt})
            # 总整流电量
            r_list.append({'tag': self.tag_prefix + suffix_rect, 'val': (oneRes[45] << 8 + oneRes[46]), 'time': tt})
            # 设备累积运行时间
            r_list.append({'tag': self.tag_prefix + suffix_runtime, 'val': (oneRes[73] << 8 + oneRes[74]), 'time': tt})
            # 是否有故障录波
            self.fault_rec = oneRes[75]
            # 设备状态及运行模式(按位)
            b_27 = bin(oneRes[27])
            bit_list_27 = [0] * (18 - len(b_27)) + list(b_27[2:])
            for i in range(16):
                if dict_suffix_27.get(i) is not None:
                    r_list.append({'tag': self.tag_prefix + dict_suffix_27[i], 'val': bit_list_27[i], 'time': tt})
            # 开关接触器状态(按位)
            b_28 = bin(oneRes[28])
            bit_list_28 = [0] * (18 - len(b_28)) + list(b_28[2:])
            for i in range(16):
                if dict_suffix_28.get(i) is not None:
                    r_list.append({'tag': self.tag_prefix + dict_suffix_28[i], 'val': bit_list_28[i], 'time': tt})

            # for i in range(len(oneRes)):
            #     if dict_suffix.get(i) is not None:
            #         r_list.append({'tag': self.tag_prefix + dict_suffix[i], 'val': oneRes[i], 'time': tt})
            for k in dict_suffix.keys():
                r_list.append({'tag': self.tag_prefix + dict_suffix[k], 'val': oneRes[k], 'time': tt})

            logger.debug("@@@@@@ --yc04--30000-- " + str(r_list))
            return r_list
        else:
            return None

    def poll_yc_03(self):
        if self.online and self.master is not None:
            oneRes = self.master.execute(self.slave, cst.READ_HOLDING_REGISTERS, 40001, 35,
                                         data_format=">" + (35 * "h"))
            logger.debug("@@@@@@ --yc03--40000-- %s:%d slave-%s, int-%s, hex- %s" % (
                self.host, self.port, self.slave, str(oneRes), self.intTupleToHexStr(oneRes)))
            oneRes = (0,) + oneRes  # 因40000的地址被删除，此处在前补个位

            tt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            r_list = []

            r_list.append({'tag': self.tag_prefix + suffix_fd_s, 'val': (oneRes[28] << 8 + oneRes[29]), 'time': tt})
            r_list.append({'tag': self.tag_prefix + suffix_rect_s, 'val': (oneRes[30] << 8 + oneRes[31]), 'time': tt})

            for k in suffix_sp.keys():
                r_list.append({'tag': self.tag_prefix + suffix_sp[k], 'val': oneRes[k], 'time': tt})

            logger.debug("@@@@@@ --yc03--40000-- " + str(r_list))
            return r_list

    def poll_fault_recode(self, redis=None):
        """
        读取故障录波数据
        :return:
        """
        if self.online and self.master is not None:
            self.reading_rec = True

            tt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            r_list = []

            quantity_of_x = 100
            p_res = ()
            for i in range(180):
                starting_address = 10001 + i * 100
                oneRes = self.master.execute(self.slave, cst.READ_INPUT_REGISTERS, starting_address, quantity_of_x,
                                             data_format=">" + (quantity_of_x * "h"))
                logger.debug("@@@@@@ --fault_recode-- %s:%d slave-%s, SA-%d, QX-%d, int-%s, hex-%s" % (
                    self.host, self.port, self.slave, starting_address, quantity_of_x, str(oneRes),
                    self.intTupleToHexStr(oneRes)))
                p_res += oneRes
                if i % 20 == 19:
                    r_list.append({'tag': self.tag_prefix + rec_params[i // 20], 'val': str(p_res), 'time': tt})
                    p_res = ()

            logger.debug("@@@@@@ --fault_recode-- " + str(r_list))

            if redis is not None:
                redis.putFaultRecData(r_list)
            # 下发录波数据已读取命令
            self.master.execute(self.slave, cst.WRITE_SINGLE_REGISTER, 40027, output_value=1)
            logger.info("@@@@@@ --YT--%d(%s)-- %s:%d slave-%d, val: %d, OK" % (40027, 'rec_read', self.host, self.port, self.slave, 1))
            self.reading_rec = False

            return r_list
        else:
            return None

    def poll_and_analysis(self):
        rr = []
        try:
            yc04 = self.poll_yc_04()
            if yc04 is not None:
                rr += yc04
        except Exception as e:
            logger.error(
                "@@@@@@ --poll_and_analysis--READ_INPUT_REGISTERS(04), 30000, 76 for %s:%d slave-%s ERROR, %s" % (
                self.host, int(self.port), self.slave, e))
        try:
            yc03 = self.poll_yc_03()
            if yc03 is not None:
                rr += yc03
        except Exception as e:
            logger.error(
                "@@@@@@ --poll_and_analysis--READ_HOLDING_REGISTERS(03), 40000, 36 for %s:%d slave-%s ERROR, %s" % (
                    self.host, int(self.port), self.slave, e))

        return rr

    def write_with_single(self, tagValList):
        """
        下发指令，此处为单个一一下发
        :param tagValList: eg [{"tag":"tag1, "val":"0"},{"tag":"tag2, "val":"2"}]
        :return:
        """
        try:
            if tagValList is not None and len(tagValList) > 0:
                for i in tagValList:
                    pp = i.get('tag').split("#")[4];
                    val = int(i.get('val'))
                    if for_write[pp] is not None and val is not None:
                        self.master.execute(self.slave, cst.WRITE_SINGLE_REGISTER, for_write[pp], output_value=val)
                        logger.info("@@@@@@ --YT--%d(%s)-- %s:%d slave-%d, val: %d, OK" % (
                            for_write[pp], pp, self.host, self.port, self.slave, val))
        except Exception as e:
            logger.error("@@@@@@ --YT--%d(%s)-- %s:%d slave-%d, val: %d error, %s" % (
                for_write[pp], pp, self.host, self.port, self.slave, val, e))

    def intTupleToHexStr(self, tuple):
        rr = "";
        for x in tuple:
            rr += hex(x) + " "
        return rr


if __name__ == '__main__':
    # my_test()
    # ae = ModbusTCP_apex_efb("221.226.253.38", 502)
    # tt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(tt)
    ae = ModbusTCP_apex_efb(host="221.226.253.38", tag_prefix="SS#DD#MM#d01#")
    # ae = ModbusTCP_apex_efb(host="127.0.0.1", tag_prefix="SS#DD#MM#d01#")
    ae.to_connect()

    ae.poll_yc_04()

    ae.poll_yc_03()

    ae.poll_fault_recode()

    tagValList = [
        {"tag": "SS#DD#MM#d02#u_fd_start", "val": "100"},
        {"tag": "SS#DD#MM#d02#u_fd_thsd", "val": "1200"}
    ]
    ae.write_with_single(tagValList)

    # hr = HandleRedis.HandleRedis(host='127.0.0.1', port=6379)
    # while True:
    #     dd = ae.poll_and_analysis()
    #     hr.putRTData(dd)
    #     print("---")
    #     time.sleep(1)

    # print(bin(22))
    # print(18 - len(bin(22)))
    # print([0] * (18 - len(bin(22))) + list(bin(22)[2:]))
    # print([0, ])
