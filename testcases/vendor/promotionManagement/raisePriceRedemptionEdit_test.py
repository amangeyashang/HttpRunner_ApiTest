# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/23 20:43'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("加价换购活动详情")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("加价换购活动详情-001")
            .with_variables(**{})
            .get("/vendor/raisePriceRedemption/edit")
            .with_params(
                **{
                    "id":"842148638850363392",
                    "memberId":"${ENV(memberId)}",
                    "userId":"${ENV(memberId)}",
                    "vendorId":"${ENV(vendorId)}",
                    "depotCode":"${ENV(vendorCode)}",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()