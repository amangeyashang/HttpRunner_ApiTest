# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 9:54'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from .createOrder_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("调用支付接口后订单状态")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("request with functions")
            .call(RequestWithFunctions)
            .export(*["summaryOrderCode"])
        ),
        Step(
            RunRequest("调用支付接口后订单状态-001")
            .with_variables(**{})
            .post("/order/orderPayState")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "orderCode":"$summaryOrderCode",
                    "summaryOrder":'true',
                    "channel":"APP"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()