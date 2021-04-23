# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/9 20:43'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from testcases.wechat.search.searchProduct_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .buildSettle_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("创建订单")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["depotCode","productCode","consigneeId"])
        ),
        Step(
            RunRequest("创建订单-001")
            .with_variables(**{})
            .post("/mallOrder/createOrder")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "consigneeId":"$consigneeId",
                    "paymentType":"WECHAT",
                    "deliverType":"USER_TRANSPORT",
                    "userRemark":"",
                    "productVos":
                        [
                            {
                                "depotCode":"$depotCode",
                                "productCode":"$productCode",
                                "quantity":1
                            }
                        ],
                    "orderClient":"wechat",
                    "userId":"${ENV(memberId)}"
                }
            )
            .extract()
            .with_jmespath("body.data.summaryOrderCode","summaryOrderCode")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()