# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 9:54'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
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
            RunRequest("调用支付接口后订单状态-001")
            .with_variables(**{})
            .post("/orderManagement/orderPayState")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "orderCode":"SOHGSPRO21031000008",
                    "summaryOrder":true,
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