# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/23 15:41'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("查看我的推荐人")
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
            RunRequest("查看我的推荐人-001")
            .with_variables(**{})
            .get("/users/findRecommendeBymemberId")
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":29.71797999388022,
                    "lon":106.63042999999999,
                    "userToken":"92b792df1b304a8d937d8119a4e50f3f",
                    "vendorCode":"$depotCode"
                }
            )
            .extract()
            .with_jmespath("body.data.VendorMemberId","VendorMemberId")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()