# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/15 17:10'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("自提校验")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("自提校验-001")
            .with_variables(**{})
            .get("/vendorOrder/getOrderDetailBySelfRecoverCode")
            .with_params(
                **{
                    "selfCheckNumber":"123456",
                    "memberId":"${ENV(memberId)}",
                    "userId":"${ENV(memberId)}",
                    "vendorId":"${ENV(vendorId)}",
                    "depotCode":"${ENV(vendorCode)}",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","查询不到该订单，请检查你的自提码")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()