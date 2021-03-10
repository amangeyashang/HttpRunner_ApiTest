# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 15:31'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("拼团订单列表")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("拼团订单列表-001")
                .with_variables(**{})
                .post("/spellGroup/findSpellGroupOrderList")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "vendorCode": "VC10003",
                    "productCode": "PD19112500000021",
                    "searchPageVo":'null'
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        )
    ]