# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/16 16:11'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .findVendorProductList_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("批量设置商品分润")
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
            RunRequest("批量设置商品分润-001")
            .with_variables(**{})
            .post("/productProfit/batchOperationProductPorfit")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "productProfitJsonArray":
                        [
                            {
                                "productId":"$productId0",
                                "productCode":"$productCode0",
                                "profitType":"AMOUNT",
                                "profitAmount":100,
                                "vendorId":"$vendorId",
                                "id":'null',
                                "profitLevel":'null'
                            },
                            {
                                "productId":"$productId1",
                                "productCode":"$productCode1",
                                "profitType":"AMOUNT",
                                "profitAmount":100,
                                "vendorId":"$vendorId",
                                "id":'null',
                                "profitLevel":'null'
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
            .assert_equal("body.msg","操作成功")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()