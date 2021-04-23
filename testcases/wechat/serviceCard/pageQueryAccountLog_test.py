# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 16:01'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("分页查询账户资金明细")
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
            RunRequest("分页查询账户资金明细-001")
            .with_variables(**{})
            .get("/account/query/pageQueryAccountLog")
            .with_params(
                **{
                    "vendorCode":"$depotCode",
                    "accountNo":"20200909000000000026",
                    "pageNo":1,
                    "pageSize":20,
                    "beginDate":"2021-03-01 00:00:00",
                    "endDate":"2021-03-31 23:59:59"
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