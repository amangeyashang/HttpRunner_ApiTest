# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/23 20:39'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .purchaseGiftList_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("买赠满赠详情")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId","purchaseGiftId"])
        ),
        Step(
            RunRequest("买赠满赠详情-001")
            .with_variables(**{})
            .get("/vendor/purchaseGiftPromotion/edit")
            .with_params(
                **{
                    "id":"$purchaseGiftId",
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
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