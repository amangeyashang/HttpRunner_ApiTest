# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/12 9:47'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("获取商家用户角色")
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
            RunRequest("获取商家用户角色-001")
            .with_variables(**{})
            .get("/vendorRegister/getUserVendorRoleByUserId")
            .with_params(
                **{
                    "userId":"$sellerId",
                    "memberId":"$sellerId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode",
                    "vendorId":"$vendorId"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()