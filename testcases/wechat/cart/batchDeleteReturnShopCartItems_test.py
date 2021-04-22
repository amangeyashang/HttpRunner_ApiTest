# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/9 20:18'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from testcases.wechat.search.searchProduct_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("批量删除返回购物车项目")
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
            RunRequest("批量删除返回购物车项目-001")
            .with_variables(**{})
            .post("/cart/batchDeleteReturnShopCartItems")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_params(
                    **{
                        "os":"min",
                        "memberId":"${ENV(memberId)}",
                        "lat":28.45362,
                        "lon":109.006128,
                        "userToken":"2c6378f841354864a19e9ffe662a719c",
                        "vendorCode":"$depotCode",
                    }
            )
            .with_json(
                {
                    "productVos":
                        [
                            {
                                "depotCode":"$depotCode",
                                "productCode":"$productCode",
                                "quantity":1
                            }
                        ]
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()