# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 11:24'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("根据user_id查询VIP信息")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export()
    )
    teststeps = [
        Step(
            RunRequest("根据user_id查询VIP信息")
                .with_variables(**{})
                .get("/vip/getPlatformVipId")
                .with_params(**{"user_id":"2494"})
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        )
    ]