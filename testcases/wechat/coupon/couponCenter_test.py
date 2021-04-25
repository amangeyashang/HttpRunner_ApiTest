# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 11:47'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.wechat.search.searchNearDepot_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("优惠券中心")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorId"])
        ),
        Step(
            RunRequest("优惠券中心-001")
            .with_variables(**{})
            .post("/vendor/couponCenter")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "couponChannelType":"WECHAT",
                    "vendorId":"$vendorId",
                }
            )
            .extract()
            .with_jmespath("body.data[0].couponTypeId","couponTypeId")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()