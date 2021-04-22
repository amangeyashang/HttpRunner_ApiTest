# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/15 11:27'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("商品列表(已上架/未上架)")
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
            RunRequest("商品列表(已上架/未上架)-已上架状态-001")
            .with_variables(**{})
            .post("/newVendorProduct/findVendorProductList")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "page": 1,
                    "size": 10,
                    "saleStatus":"ON_SALE",
                    "vendorId": "$vendorId"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("商品列表(已上架/未上架)-未上架状态-002")
            .with_variables(**{})
            .post("/newVendorProduct/findVendorProductList")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "page": 1,
                    "size": 10,
                    "saleStatus":"OFF_SALE",
                    "vendorId": "$vendorId"
                }
            )
            .extract()
            .with_jmespath("body.data.content[0].productCode","productCode0")
            .with_jmespath("body.data.content[1].productCode","productCode1")
            .with_jmespath("body.data.content[0].id","productId0")
            .with_jmespath("body.data.content[1].id","productId1")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()