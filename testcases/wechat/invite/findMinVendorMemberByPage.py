# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/11 9:21'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("查询我的推荐下级列表")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("查询我的推荐下级列表-001")
                .with_variables(**{})
                .post("/users/findMinVendorMemberByPage")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "vendorMemberId":41,
                    "page":0,
                    "size":20
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        )
    ]