# -*- coding: utf-8 -*-

"""
------------------------------------------------

describe: 

base_info:
    __author__ = "PyGo"
    __time__ = "2024/9/3 22:25"
    __version__ = "v.1.0.0"
    __mail__ = "gaoming971366@163.com"
    __blog__ = "www.pygo2.top"
    __project__ = "fastapi-qr"

usage:

design:

reference urls:

python version:
    python3


Enjoy the good life everyday！！!
Life is short, I use python.

------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python zlxcx.py
# ------------------------------------------------------------
import requests

from deploy.utils.status import Status
from deploy.utils.status_value import StatusEnum as Status_enum, \
    StatusMsg as Status_msg, StatusCode as Status_code


class ApiService(object):
    """
    API Service
    """

    # zlxcx_process
    zlxcx_process_params = [
        'xmbh',
        'year',
        'quarter'
    ]
    ZLXCX_PROCESS_YEAR_LIST = [2023, 2024]
    ZLXCX_PROCESS_QUARTER_LIST = {
        "第一季度": 0,
        "第二季度": 1,
        "第三季度": 2,
        "第四季度": 3,
    }

    def __init__(self):
        """
        ApiService class initialize
        """
        super(ApiService, self).__init__()

    def __str__(self):
        print("ZlxcxService class.")

    def __repr__(self):
        self.__str__()

    def zlxcx_token(self) -> dict:
        url = "http://tmis.pasok.cn/tmis/api/loginToken?_code=aHXCeyJwYXNzd29yZCI6Ijc3QjhCRjUxRUFFOUJCODVBMEM0RDk4QzcwM0ZGNjc1IiwidXNlcm5hbWUiOiIxMjE3NCJ9n5Ws"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response_json = response.json()
        if response_json.get('code') == 0:
            return {"token": response_json.get("data")}
        else:
            return {"token": ""}

    def zlxcx_process(self, params: dict) -> dict:
        """
        质量小程序: 过程检查
        :return: json data
        """
        # ====================== parameters check ======================
        if not params:
            return Status(
                Status_code.CODE_400_REQUEST_PARAMETER_MISS.value,
                Status_enum.FAILURE.value,
                Status_msg.get(400),
                {}
            ).status_body

        # new parameters
        new_params = dict()
        for k, v in params.items():
            if not k: continue
            if k not in self.zlxcx_process_params:
                return Status(
                    Status_code.CODE_401_REQUEST_PARAMETER_ILLEGAL.value,
                    Status_enum.FAILURE.value,
                    '请求参数%s不合法' % k,
                    {}
                ).status_body

            if not v:
                return Status(
                    Status_code.CODE_403_REQUEST_PARAMETER_NOT_NULL.value,
                    Status_enum.FAILURE.value,
                    '请求参数%s不允许为空' % k,
                    {}
                ).status_body

            if k == 'year' and int(v) not in self.ZLXCX_PROCESS_YEAR_LIST:
                # 年份参数
                return Status(
                    Status_code.CODE_404_REQUEST_PARAMETER_VALUE_ERROR.value,
                    Status_enum.FAILURE.value,
                    Status_msg.get(404),
                    {}
                ).status_body
            elif k == 'quarter' and v not in self.ZLXCX_PROCESS_QUARTER_LIST.keys():
                # 季度参数
                return Status(
                    Status_code.CODE_404_REQUEST_PARAMETER_VALUE_ERROR.value,
                    Status_enum.FAILURE.value,
                    Status_msg.get(404),
                    {}
                ).status_body

            new_params[k] = str(v)

        # 季度INDEX
        quarter_index = self.ZLXCX_PROCESS_QUARTER_LIST.get(new_params.get('quarter'))
        # 删除季度参数
        del new_params['quarter']
        other = {
            "gzsj": "",
            "zxjg": "",
            "jcpl": "",
            "zblx": "",
            "db": "dn0"
        }
        querystring = {**new_params, **other}
        url = "http://tmis.pasok.cn/tmis/pmp/zkgl/getZkjgList"
        token = self.zlxcx_token()
        if not token or not token.get('token'):
            return Status(
                Status_code.CODE_903_OTHER_THREE_API_TOKEN_FAILURE.value,
                Status_enum.FAILURE.value,
                '质量API TOKEN初始化失败',
                {}
            ).status_body

        payload = {}
        headers = {
            'accept': "application/json, text/plain, */*",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh,zh-CN;q=0.9,en;q=0.8,ru;q=0.7",
            'cache-control': "no-cache,no-cache",
            'connection': "keep-alive",
            # 'cookie': "JSESSIONID=BDDC181C4A33208A91B10EB39066C200",
            'host': "tmis.pasok.cn",
            'pragma': "no-cache",
            'referer': "http://tmis.pasok.cn/",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            'x-token': token.get('token'),
            'Postman-Token': "58d1a484-e8a6-4438-8cab-564f535f4dc2"
        }

        # 过程检查指标
        ZB = {
            44: "数据备份",
            26: "效果评估汇报",
            28: "效果评估评审",
            46: "效果评估咨询人员配置",
            54: "培训 / 调研 / 辅导 / 座谈会次数",
            52: "系统使用次数",
            25: "总调度跑批时长",
            22: "工资确认单",
            49: "一把手拜访",
            2: "阶段工作成果汇报",
            # ----------- 暂不展示 -----------
            # 36: "五结合评审",
            # 5: "制度评审",
            # 24: "价格测算",
            # 39: "咨询人员配置",
            # 50: "工资兑现流程",
            # 51: "当年首次按新办法兑现",
            # 6: "工资核对表",
            # 16: "效果自评",
            # 17: "成绩单规划清单",
            # 18: "成绩单一览表",
            # 19: "一把手认知评估",
            # 15: "续约汇报"
        }
        """
        zxqk为2长度指标:
            总调度跑批时长
        zxqk为3长度指标:
            效果评估汇报 效果评估评审 效果评估咨询人员配置
        zxqk为4长度指标:
            数据备份 系统使用次数 工资确认单
            培训/调研/辅导/座谈会次数 阶段工作成果汇报 一把手拜访
        """
        ZB_ZXQK_2 = [25]
        ZB_ZXQK_3 = [26, 28, 46]
        ZB_ZXQK_4 = [22, 44, 52, 54, 2, 49]

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        res = dict()
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("code") == 0:
                response_json_data_list = response_json.get('data').get('list')
                res['info'] = response_json.get('data').get('info')
                zb_list = list()
                for item in response_json_data_list:
                    if not item:
                        continue

                    # print("%s:%s" % (item.get('zbid'), item.get('zbmc')))
                    zb = dict()
                    # 指标ID
                    zb_id = item.get('zbid')
                    if int(zb_id) not in ZB.keys():
                        # 只统计展示指标
                        continue
                    zb['zbid'] = zb_id
                    # 指标名称
                    zb['zbmc'] = item.get('zbmc')
                    # 工作事件
                    zb['gzsj'] = item.get('gzsj')
                    # 检查频率
                    zb['jcpl'] = item.get('jcpl')
                    # 指标类型
                    zb['zblx'] = item.get('zblx')
                    # 质量标准
                    zb['zlbz'] = item.get('zlbz')
                    # 检查标准
                    zb['jcbz'] = item.get('jcbz')
                    # 扣罚标准
                    zb['kfbz'] = item.get('kfbz')
                    # 关联模型节点
                    zb['zjmx'] = item.get('zjmx')
                    # 手工指标SQL
                    # zb['sgzbsql'] = item.get('sgzbsql')
                    # 项目计划
                    zb['xmjh'] = item.get('xmjh')
                    # SF说明
                    zb['sfms'] = item.get('sfms')
                    # JMGZ
                    zb['jmgz'] = getattr(item, 'jmgz', "")
                    # 执行情况（是个list类型，并且根据月度/季度/年度数据长度不等，需要进行for循环）
                    # 只展示查询季度数据
                    zxqk_list = item.get('zxqk')
                    if zb_id in ZB_ZXQK_4:
                        zb['zxqk'] = zxqk_list[quarter_index].get('zxjgmc')
                    elif zb_id in ZB_ZXQK_3:
                        # 效果评估
                        if quarter_index in [0, 1, 3]:
                            _index = 0
                        elif quarter_index in [4]:
                            _index = 1
                        else:
                            _index = 0
                        zb['zxqk'] = zxqk_list[_index].get('zxjgmc')
                    elif zb_id in ZB_ZXQK_2:
                        # 调度时长优化
                        if quarter_index in [0, 1]:
                            _index = 0
                        else:
                            _index = 1
                        zb['zxqk'] = zxqk_list[_index].get('zxjgmc')
                    else:
                        zb['zxqk'] = '/'
                    zb_list.append(zb)
                res['list'] = zb_list

        return Status(
            Status_code.CODE_100_SUCCESS.value,
            Status_enum.SUCCESS.value,
            Status_msg.get(100),
            res
        ).status_body


