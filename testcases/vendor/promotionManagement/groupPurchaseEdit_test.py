# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/23 20:47'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("拼团促销详情")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("拼团促销详情-001")
            .with_variables(**{})
            .get("/vendor/groupPurchase/edit")
            .with_params(
                **{
                    "id":"867229710411657216",
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