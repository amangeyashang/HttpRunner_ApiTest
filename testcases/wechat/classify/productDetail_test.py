# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 15:19'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from testcases.wechat.search.searchProduct_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("商品详情")
        .variables(**{})
        .base_url("${ENV(base_url_wechat_develop_rest)}")
        .verify(False)
        .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["depotCode","productCode"])
        ),
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
                    "depotCode": "$depotCode",
                    "productCode": "$productCode",
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()