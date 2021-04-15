# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/16 10:03'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("查询商家弹窗配置")
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
            RunRequest("查询商家弹窗配置-001")
            .with_variables(**{})
            .get("/vendorIndexApiService/findPopupConfigByPage")
            .with_params(
                **{
                    "page":1,
                    "size":10,
                    "memberId":"$memberId",
                    "userId":"$memberId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
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