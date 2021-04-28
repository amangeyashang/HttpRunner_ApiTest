# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/15 11:45'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("商品分润设置列表")
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
            RunRequest("商品分润设置列表-001")
            .with_variables(**{})
            .post("/newVendorProduct/findVendorProdcutListForProductProfit")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "categoryId":"",
                    "page":1,
                    "productName":"",
                    "barCode":"",
                    "productCode":"",
                    "saleStatus":"OFF_SALE",
                    "size":10,
                    "vendorId": "$vendorId"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()