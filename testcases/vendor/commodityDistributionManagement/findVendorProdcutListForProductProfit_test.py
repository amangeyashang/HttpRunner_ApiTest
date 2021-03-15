# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/15 11:45'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("商品分润设置列表")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
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
                    "page": 1,
                    "size": 10,
                    "saleStatus":"OFF_SALE",
                    "vendorId": "${ENV(vendorId)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()