# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/23 17:28'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("确认接单")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("确认接单-001")
            .with_variables(**{})
            .get("/vendorOrder/orderAffirmState")
            .with_params(
                **{
                    "order_code":"STHGSPRO21032300013",
                    "memberId":"${ENV(memberId)}",
                    "userId":"${ENV(memberId)}",
                    "vendorId":"${ENV(vendorId)}",
                    "depotCode":"${ENV(vendorCode)}",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","该订单状态异常。")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()