# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/16 10:16'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("查询商家弹窗配置")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("查询商家弹窗配置-001")
            .with_variables(**{})
            .get("/venPackingChargesConfig/findByVendorCode")
            .with_params(
                **{
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