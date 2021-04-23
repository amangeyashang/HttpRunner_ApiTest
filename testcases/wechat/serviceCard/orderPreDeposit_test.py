# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/23 15:54'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("生成预存赠品订单")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["depotCode"])
        ),
        Step(
            RunRequest("生成预存赠品订单-001")
            .with_variables(**{})
            .post("/promotion/preDeposit/orderPreDeposit")
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
                    "userToken":"684f2aa256a6408980cbb1f56602e250",
                    "vendorCode":"$depotCode"
                }
            )
            .with_json(
                {
                    "bizNo":"20201231PT9399053436",
                    "clientType":"wechat"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","预存活动订单流水不在预期状态")
            .assert_equal("body.status","F")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()