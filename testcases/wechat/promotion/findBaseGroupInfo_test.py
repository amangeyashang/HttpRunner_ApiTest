# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/22 11:30'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("拼团详情")
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
            RunRequest("拼团详情-001")
            .with_variables(**{})
            .get("/spellGroup/findBaseGroupInfo")
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
                    "lat":"29.71797999388022",
                    "lon":"106.63042999999999",
                    "userToken":"c857660825954391ab036eed074861ad",
                    "vendorCode":"$depotCode",
                    "baseId":"826994780838891520"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()