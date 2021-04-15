# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/16 9:57'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("获取店铺首页模版列表")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId"])
        ),
        Step(
            RunRequest("获取店铺首页模版列表-001")
            .with_variables(**{})
            .post("/vendorIndexApiService/getTemplate")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "vendorCode":"$vendorCode"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()