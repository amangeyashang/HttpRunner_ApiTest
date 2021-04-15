# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/15 11:00'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("加价换购状态更新")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId"])
        ),
        Step(
            RunRequest("加价换购状态更新-001")
            .with_variables(**{})
            .get("/vendor/raisePriceRedemption/statusToggle")
            .with_params(
                **{
                    "page":1,
                    "size":10,
                    "promotionActivity":"ALL",
                    "name":"",
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .extract()
            .with_jmespath("body.data.content[0].id","raisePriceRedemptionId")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()