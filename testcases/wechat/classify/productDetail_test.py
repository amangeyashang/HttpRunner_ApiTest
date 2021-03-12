# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 15:19'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("商品详情")
        .variables(**{})
        .base_url("${ENV(base_url_wechat_online)}")
        .verify(False)
        .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("商品详情-001")
            .with_variables(**{})
            .post("/product/productDetail")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "depotCode": "${ENV(vendorCode)}",
                    "productCode": "PD19123000000009",
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()