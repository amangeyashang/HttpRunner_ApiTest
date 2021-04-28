# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/21 16:07'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .pageQueryPurchaseProduct_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("创建采购单")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId","vendorName","productCode1","minPurchaseQuantity1","productCode2","minPurchaseQuantity2"])
        ),
        Step(
            RunRequest("创建采购单-001")
            .with_variables(**{})
            .post("/tob/purchaseOrder/createPurchaseOrder")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "creator":"测试2",
                    "memo":"",
                    "purchaseOrderItemInfoList":
                        [
                            {
                                "productCode":"$productCode1",
                                "vendorQuantity":"$minPurchaseQuantity1"
                            },
                            {
                                "productCode":"$productCode2",
                                "vendorQuantity":"$minPurchaseQuantity2"
                            },
                        ],
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode",
                    "vendorName":"$vendorName"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","成功")
            .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()