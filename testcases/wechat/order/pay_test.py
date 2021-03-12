# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/9 20:51'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("支付")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("支付-001")
                .with_variables(**{})
                .post("/orderManagement/pay")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "channel":"WEB",
                    "orderCode":"SOHGSPRO21030900023",
                    "summaryOrder":'true',
                    "paymentChannel":"WechatPay",
                    "tradeType":"JSAPI",
                    "payAccount":"onQ7N4inZqv-E8LmodEs0T2_-Vjg"
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()