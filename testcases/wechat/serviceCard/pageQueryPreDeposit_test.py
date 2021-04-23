# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 11:37'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("分页查询预存活动订单流水列表")
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
            RunRequest("分页查询预存活动订单流水列表-未领取-001")
            .with_variables(**{})
            .post("/promotion/preDeposit/pageQueryPreDeposit")
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
                    "vendorCode":"$depotCode",

                }
            )
            .with_json(
                {
                    "vendorCode":"$depotCode",
                    "userId":"${ENV(memberId)}",
                    "pageInfo":
                        {
                            "pageNo":1,
                            "pageSize":10
                        },
                    "status":"P"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","成功")
            .assert_equal("body.status","S")
        ),
        Step(
            RunRequest("分页查询预存活动订单流水列表-已领取-002")
            .with_variables(**{})
            .post("/promotion/preDeposit/pageQueryPreDeposit")
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
                    "vendorCode":"$depotCode",

                }
            )
            .with_json(
                {
                    "vendorCode":"$depotCode",
                    "userId":"${ENV(memberId)}",
                    "pageInfo":
                        {
                            "pageNo":1,
                            "pageSize":10
                        },
                    "status":"S"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","成功")
            .assert_equal("body.status","S")
        ),
        Step(
            RunRequest("分页查询预存活动订单流水列表-已过期-003")
            .with_variables(**{})
            .post("/promotion/preDeposit/pageQueryPreDeposit")
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
                    "vendorCode":"$depotCode",

                }
            )
            .with_json(
                {
                    "vendorCode":"$depotCode",
                    "userId":"${ENV(memberId)}",
                    "pageInfo":
                        {
                            "pageNo":1,
                            "pageSize":10
                        },
                    "status":"EXPIRED"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","成功")
            .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()