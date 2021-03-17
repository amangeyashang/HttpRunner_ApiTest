# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 11:07'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("删除订单")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("删除订单-001")
            .with_variables(**{})
            .get("/order/deleteOrder")
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat": 29.71797999388022,
                    "lon": 106.63042999999999,
                    "userToken":"92b792df1b304a8d937d8119a4e50f3f",
                    "vendorCode":"${ENV(vendorCode)}",
                    "orderCode":"SOHGSPRO21031000008"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()