# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/10 14:17'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("查询有效预存活动")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("查询有效预存活动-001")
                .with_variables(**{})
                .post("/promotion/preDeposit/queryValidPreDepositPromotion")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "vendorCode":"VC10003"
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.message","成功")
                .assert_equal("body.status","S")
        )
    ]