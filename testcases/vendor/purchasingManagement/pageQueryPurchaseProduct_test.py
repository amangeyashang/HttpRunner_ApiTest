# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/21 15:12'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("采购商品分页")
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
            RunRequest("采购商品分页-001")
            .with_variables(**{})
            .post("/tob/purchase/pageQueryPurchaseProduct")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "categoryIdF": "",
                    "categoryIdS": "",
                    "categoryId": "",
                    "pageInfo": {
                        "pageNo": 1,
                        "pageSize": 20,
                        "total": 0
                    },
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .extract()
            .with_jmespath("body.infoList[0].productCode","productCode1")
            .with_jmespath("body.infoList[0].minPurchaseQuantity","minPurchaseQuantity1")
            .with_jmespath("body.infoList[1].productCode","productCode2")
            .with_jmespath("body.infoList[1].minPurchaseQuantity","minPurchaseQuantity2")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","成功")
            .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()