# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 10:58'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("获取模版详情")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("获取模板详情-001")
            .with_variables(**{})
            .post("/indexApiService/templateDetails")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "vendorCode": "$vendorCode",
                    "templateId": "$templateId1",
                    "advertisementType": "$templateType1"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]