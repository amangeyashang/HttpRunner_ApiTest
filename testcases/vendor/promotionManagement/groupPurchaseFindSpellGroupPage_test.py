# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/15 14:27'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .groupPurchaseList_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("参团详情")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
                .call(RequestWithFunctions)
                .export(*["vendorCode","sellerId","vendorId","groupPurchaseId"])
        ),
        Step(
            RunRequest("参团详情-001")
            .with_variables(**{})
            .post("/vendor/groupPurchase/findSpellGroupPage")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "promotionId":"$groupPurchaseId",
                    "groupState":"ALL",
                    "searchPageVo":{"pageIndex":1,"pageSize":10},
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