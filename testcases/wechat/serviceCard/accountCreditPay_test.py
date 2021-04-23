# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 15:57'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("用户账户Account 充值")
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
            RunRequest("用户账户Account充值-001")
            .with_variables(**{})
            .post("/account/accountCreditPay")
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
                "memberId":"${ENV(memberId)}",
                "amount":1,
                "channel":"WEB",
                "paymentChannel":"WechatPay",
                "tradeType":"JSAPI",
                "payAccount":"onQ7N4inZqv-E8LmodEs0T2_-Vjg",
                "promotionId":7
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()