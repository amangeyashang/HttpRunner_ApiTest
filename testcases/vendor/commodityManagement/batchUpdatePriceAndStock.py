# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/16 17:25'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .findVendorProductList_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("批量修改价格和库存")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
                .call(RequestWithFunctions)
                .export(*["vendorCode","sellerId","vendorId","productId0","productCode0","productId1","productCode1"])
        ),
        Step(
            RunRequest("批量修改价格和库存-001")
            .with_variables(**{})
            .post("/newVendorProduct/batchUpdatePriceAndStock")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "batchUpdatePriceAndStockInfoList":
                        [
                            {
                                "productId":"$productId0",
                                "productCode":"$productCode0",
                                "costPrice":"0.00",
                                "marketPrice":"4.00",
                                "finalPrice":"4.50",
                                "stock":100,
                                "stockWarnValue":1
                            },
                            {
                                "productId":"$productId1",
                                "productCode":"$productCode1",
                                "costPrice":"1.00",
                                "marketPrice":"2.00",
                                "finalPrice":"5.00",
                                "stock":100,
                                "stockWarnValue":1
                            }
                        ],
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