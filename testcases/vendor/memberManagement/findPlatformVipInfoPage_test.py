# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/15 18:06'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("商家VIP列表")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("商家VIP列表-001")
            .with_variables(**{})
            .get("/vendorVip/findPlatformVipInfoPage")
            .with_params(
                **{
                    "vipVendorId":"546520236057329664",
                    "channelType":"",
                    "phone":"",
                    "startTime":"",
                    "endTime":"",
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